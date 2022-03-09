"""
find most effecient path from warehouse to city
"""
from collections import defaultdict
from itertools import product

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        
        self.distance = 9999
        self.color = 'black'
    
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
            
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
        
    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
        
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'
            
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
    
    def reset(self):
        for key in sorted(list(self.vertices.keys())):
            self.vertices[key].distance = 9999
            self.vertices[key].color = 'black'


def main():
    with open ("shoppee/2021/pset2","r") as f:
        t = f.readline()
        t = t.split()
        cities = int(t[0])
        warehouses = int(t[1])
        roads = int(t[2])
        network = []
        wh = defaultdict(list)
        orders = {}
        for i in range (roads):
            rd = f.readline()
            rd = rd.split()
            network.append(rd)
        city = []
        for i in range (warehouses):
            w = f.readline()
            w = w.split()
            city.append(w[2])
            wh[w[2]].append(w[1])
            wh[w[2]].append(w[0])
        x = f.readline()
        x = x.split() 
        m = int(x[0])
        for i in range (m):
            o = f.readline()
            o = o.split()
            try:
                orders[o[1]]+=int(o[0])
            except:
                orders[o[1]] = int(o[0])
    g = Graph()
    temp = {}
    for i in range(len(city)):
        temp[i] = Vertex(str(city[i]))
        g.add_vertex(temp[i])
    for i in range(1,cities):
        g.add_vertex(Vertex(str(i)))
    for x in network:
        g.add_edge(x[0], x[1])
    
    perm = {}
    for cities in temp:
        perm[cities] = [0]
        g.bfs(temp[cities])
        for keys in orders:
            perm[cities].append(int(g.vertices[keys].distance) * int(wh[city[cities]][0]))
        g.reset()
    print(perm)

    sumsofar = []
    for x in product(*perm.values()):
        for i in range(len(x)):
            x[i] * min(wh[city[cities]][0], orders)
        


        
if __name__ == '__main__':
    main()