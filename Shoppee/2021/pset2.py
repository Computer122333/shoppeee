"""
find most effecient path from warehouse to city
"""
from collections import defaultdict

def main():
    with open ("shoppee/2021/pset2","r") as f:
        t = f.readline()
        t = t.split()
        cities = int(t[0])
        warehouses = int(t[1])
        roads = int(t[2])
        network = []
        wh = defaultdict(list)
        orders = []
        for i in range (roads):
            rd = f.readline()
            rd = rd.split()
            network.append(rd)
        for i in range (warehouses):
            w = f.readline()
            w = w.split()
            wh[w[2]].append(w[1])
            wh[w[2]].append(w[0])
        x = f.readline()
        x = x.split() 
        m = int(x[0])
        for i in range (m):
            o = f.readline()
            o = o.split()
            orders.append(o)
        print(network,wh,orders)
        
if __name__ == '__main__':
    main()