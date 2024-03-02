n = int(input())

for i in range(1, n*2):
    if i < n:
        print(' ' * (n-i), end='')
        print('* ' * i)
    else:
        print(' ' * (i-n), end='')
        print('* ' * (2*n - i))