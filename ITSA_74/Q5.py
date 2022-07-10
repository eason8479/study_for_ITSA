def decode_list(li):
    li = [ord(i) for i in li]
    li.reverse()

    decode = 0
    text = []

    for i in li:
        if (i >= 48) and (i <= 57):
            decode = (i-48)

        else:
            i += decode
            if (i > 90):
                i -= 26
            text.append(chr(i))
    
    text.reverse()
    print(''.join(text))


def read_input(n):
    table = []
    for _ in range (n):
        li = input().split()
        table.append(li)
    return (table)

n = int(input())
table = read_input(n)
for i in range (len(table)):
    decode_list(table[i])   