r = float(input())
n = int(input())
q = int(input())

total = 0

for i in range (n):
    total += q
    total = total*(1+r)

print (int(total))