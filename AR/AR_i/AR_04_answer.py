# code phase 1
while True:
    try:
        num = int(input())
        for step in range(num):
            row, col = (int(n) for n in input().split())

            graph = []
            for i in range(row):
                lt = [int(n) for n in input().split()]
                graph.append(lt)
            
            for i in range(row):
                for j in range(col):
                    if graph[i][j] == 0:
                        print("_ ", end='')
                    else:
                        if i>0 and graph[i-1][j]==0:
                            print("0 ", end='')
                        elif i<row-1 and graph[i+1][j]==0:
                            print("0 ", end='')
                        elif j>0 and graph[i][j-1]==0:
                            print("0 ", end='')
                        elif j<col-1 and graph[i][j+1]==0:
                            print("0 ", end='')
                        else:
                            print("_ ", end='')
                print()
            if step != num-1: 
                print()
    except:
        break
