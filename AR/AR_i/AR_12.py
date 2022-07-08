def find_seat (li):

    left_move = li[0]
    right_move = li[1]
    total = li[2]

    cir = [i for i in range (total)]

    remove_pos = 0
    total -= 1

    for i in range (total):
        
        if(i%2 == 0):
            turn = right_move
            
            while(turn > 0):
                remove_pos += 1
                
                if (remove_pos == total+1):
                    remove_pos = 0

                if (cir [remove_pos] != -1):
                    turn -= 1

                
        
        elif(i%2 == 1):
            turn = left_move
            
            while(turn > 0):
                remove_pos -= 1
                
                if (remove_pos == -1):
                    remove_pos = total

                if (cir [remove_pos] != -1):
                    turn -= 1
                    
        cir[remove_pos] = -1

    answer = 0
    for i in cir:
        if (i != -1):
            answer = i+1
            break

    print(answer)

turn = int(input())
li = []
for i in range (turn):
    tmp = input().split()
    for n in range (len(tmp)):
        tmp[n] = int(tmp[n])
    li.append(tmp)

for sub in li:
    find_seat(sub)
