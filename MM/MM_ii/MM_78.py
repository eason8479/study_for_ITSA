def prefect_finder(n):
    num = 0
    if (n%10 == 6) or (n%100 == 28):
        for i in range (1,int(n/2)+2):
            if (n%i == 0):
                num += i
        if (num == n):
            return True
        else:
            return False

low, upper = input().split()
prefect_list = []

for i in range (int(low), int(upper)+1):
    if prefect_finder(i):
        prefect_list.append(i)

if (len (prefect_list) == 0):
    print("null")
else:
    text = ''
    for i in range (len(prefect_list)):
        if (i == len(prefect_list)-1):
            text = text + str(prefect_list[i])
        else:
            text = text + str(prefect_list[i]) +' '
    print(text)