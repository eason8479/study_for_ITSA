class num_57:
    def __init__(self,value):
        self.value = value
        self.plus_5 = False
        self.plus_7 = False

class next_num:
    def __init__(self,val,location,_5or7):
        self.val = val
        self.location = location
        self._5or7 = _5or7
        

step = int(input())-1

list_57 = [num_57(0)]
list_numonly = [0]

for i in range (step):
    
    p_next = []
    for n in range (len(list_57)):
        if not (list_57[n].plus_5):
            if not (list_57[n].value + 5 in list_numonly):
                p_next.append(next_num(list_57[n].value + 5 , n , 5))

        if not (list_57[n].plus_7):
            if not (list_57[n].value + 7 in list_numonly):
                p_next.append(next_num(list_57[n].value + 7 , n , 7))
    
    n_num = p_next[0]
    for n in range (len(p_next)):
        if (p_next[n].val < n_num.val):
            n_num = p_next[n]
    
    list_57.append(num_57(n_num.val))
    list_numonly.append(n_num.val)

    if(n_num._5or7 == 5):
        list_57[n_num.location].plus_5 = True
    elif(n_num._5or7 == 7):
        list_57[n_num.location].plus_7 = True

print(list_numonly[step])