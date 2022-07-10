def count_triangle(n):
    num = 0

    for i in range (1,n):
        if (n-2*i)>0 :
            num += (n-2*i)*(i-1)+(i*(i-1))/2
        else:
            num += (n-i)*(n-i-1)/2

    print (int(num))

turn = int(input())
li = input().split()

for i in range (turn):
    count_triangle(int(li[i]))