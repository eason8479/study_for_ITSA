def read_input(n):
    table = []
    for _ in range (n):
        input()
        li = input().split()
        li = [int(i) for i in li]
        table.append(li)
    return (table)

def find_longest(li):
    c_num = 0
    num_length = [0 for _ in range (10)]
    for i in range (len(li)):
        if (li[i] != c_num):
            c_num = li[i]
        num_length[c_num] += 1
    long = 0
    for i in range (10):
        if (num_length[i] > long):
            long = num_length[i]
    print(long)

n = int(input())
table = read_input(n)

for li in table:
    find_longest(li)