x, y = input().split()

x = int(x)
y = int(y)

if (x**2+y**2 <= 10000):
    print('inside')
else:
    print('outside')