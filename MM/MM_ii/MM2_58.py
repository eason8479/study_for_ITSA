from math import ceil
def int_dect(n):
    if (n == int(n)):
        return True
    else:
        return False
li = [int(i) for i in input().split(",")]
a = li[0]
for i in range (len(li)):
    li[i] = li[i]/a
b = li[1]
c = li[2]
for x in range (ceil(c)+1):
    ans = (c-x)/b
    if int_dect(ans):
        print(x, end=',')
        print(int(ans))