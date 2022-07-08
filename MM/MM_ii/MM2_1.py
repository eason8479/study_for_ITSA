import math

def check_prime(x):
    limit = int(math.ceil(math.sqrt(x)))

    for i in range (2,limit+1):
        if (x%i == 0):
            return 0
    return x

p_num = int(input())
p_num -= 1

p_li = [2]
p_total = 2
current_num = 3

while(p_num != 0):
    tmp = check_prime(current_num)
    
    if(tmp != 0):
        p_li.append(tmp)
        p_total += tmp
        p_num -= 1
    
    current_num += 1

for i in range (len(p_li)):
    print(p_li[i], end=',')
print()
print(p_total)


