class node:
    def __init__(self, num, conn):
        self.num = num
        self.conn = conn
        self.cost = 0
    
    def cal_cost(self):
        for i in range (10):
            self.cost += self.conn[i]
    
    def simp(self):
        new_conn = []
        for i in range (10):
            if (self.conn[i]):
                new_conn.append(i)
        self.conn = new_conn

def cal_path(path_now):
    node_now = path_now[len(path_now)-1]
    path_next = []
    
    for i in (node_table[node_now].conn):
        if not (i in path_now):
            tmp = []
            for n in (path_now):
                tmp.append(n)
            tmp.append(i)
            path_next.append(tmp)

    if (path_next != []):
        return(path_next)

tmp1 = []
node_table = []

#read input
for _ in range (10):
    tmp1.append(input().split())

for i in range (10):
    tmp2 = []
    for n in range (10):
        tmp2.append(int(tmp1[i][n]))
    node_table.append(node(i, tmp2))

#cal cost
for i in range(10):
    node_table[i].cal_cost()
    node_table[i].simp()

path = [[0]]
result = []

for _ in range (7):
    for i in (path):
        if (9 in i):
            result.append(i)
            path.remove(i)
        else:
            tmp = cal_path(i)
            if (tmp != None):
                for n in (tmp):
                  path.append(n)

cost = 100000
path = None
for i in (result):
    cost_tmp = 0
    for n in i:
        cost_tmp = cost_tmp + node_table[n].cost
    if (cost_tmp < cost):
        cost = cost_tmp
        path = i

text = ''
for i in range (len(path)):
    if (i == len(path)-1):
        text = text + str(path[i])
    else:
        text = text + str(path[i]) + '-'

text = text + ' : ' + str(cost)
print(text)