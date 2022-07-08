str1 = input().split(' ')
result = 0

for i in range(6):
    result += int(str1[i])**3

print(result)
