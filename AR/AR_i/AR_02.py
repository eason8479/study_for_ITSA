li = input().split()
li.reverse()
text = ''
for i in li:
    text = text + str(i) + ' '
print(text.strip())
