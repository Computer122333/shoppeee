"""
Given imput statement of
No. test cases
no. of days (N) No. of trees(M)
trees daily

decide wether to 
1. not cross
2. cross to certain point
3. cross completely

maintain highest health"""
import time

def stay(list):
    max, counter = 0,0
    for i in range(len(list)):
        counter+=int(list[i])
        if counter > max:
            max = counter
    return max

def move(list):
    return sum(int(i) for i in list)

def main():
    start_time = time.time()
    answer = []
    with open("shoppee/2021/pset1","r") as f:
        t = f.readline()
        t = t.strip().split()
        testcases = int(t[0])
        while testcases != 0:
            n = f.readline()
            n = n.strip().split()
            days = int(n[0])
            trees = []
            for i in range(days):
                m = f.readline()
                m = m.strip().split()
                trees.append(m)

            list = []
            list.append(stay(trees[0]))
            list.append(move(trees[0]))
            print(list)
            temp = []

            counter = 1
            while counter < days:
                #left to right
                for i in range(0,len(list),2):
                    temp.append(list[i]+stay(trees[counter]))
                    temp.append(list[i]+move(trees[counter]))

                #right to left
                for i in range(1,len(list),2):
                    temp.append(list[i]+move(trees[counter]))
                    temp.append(list[i]+stay(trees[counter][::-1]))
                list.clear()

                if temp[0] > temp[2]:
                    list.append(temp[0])
                else:
                    list.append(temp[2])


                if temp[1] > temp[3]:
                    list.append(temp[1])
                else:
                    list.append(temp[3])
                print(list)

                temp.clear()
                counter+=1
            answer.append(max(list))
            testcases-=1
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    return answer
    
print(main())