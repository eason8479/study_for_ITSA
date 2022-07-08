turn = int(input())
ip = [[] for _ in range (turn)]

#read input
for i in range (turn):

    tmp = input().split()
    
    coloum = int(tmp[0])
    row = int(tmp[1])

    for n in range (coloum):
        ip[i].append(input().split())
     

for i in range (turn):
    
    op = []
     
    for a in range (len(ip[i])):
        tmp = [0 for _ in range (row)]

        for b in range (len(ip[i][a])):
            
            if (ip[i][a][b] == '0'):
                tmp[b] = '_'
            
            elif (ip[i][a][b] == '1'):
                edge = 0
                if (a != 0):
                    if(ip[i][a-1][b] == '0'):
                        edge = 1
                
                if (b != 0):
                    if(ip[i][a][b-1] == '0'):
                        edge = 1

                if (a < len(ip[i])-1):
                    if(ip[i][a+1][b] == '0'):
                        edge = 1
                
                if (b < len(ip[i][a])-1):
                    if(ip[i][a][b+1] == '0'):
                        edge = 1

                if(edge == 1):
                    tmp[b] = 0
                elif(edge == 0):
                    tmp[b] = '_'
        
        op.append(tmp)

    if (turn != 0):
        print()
    for a in range (len(ip[i])):
        for b in range (len(ip[i][a])):
            print(op[a][b], end = ' ')
        print()

