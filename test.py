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
            while (i > 90):
                i -= 26
            text.append(chr(i))

    text.reverse()
    ''.join(text)
    print(text)

li = input().split()

decode_list(li)