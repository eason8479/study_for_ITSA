from math import ceil


m = int(input())
li = []

for i in range (m):
    li.append(input().split())
    li[i][0] = float(li[i][0])-10
    li[i][1] = float(li[i][1])-10

for i in li:    
    p = 10 - int((i[0]**2+i[1]**2)**0.5)
    if (p >= 1):
        print(p)
    else:
        print(0)

