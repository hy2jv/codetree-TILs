n = int(input())
odd, even = 1, 2
x = 0
for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            x+= odd
            print(x, end=' ')
        else:
            x+=even
            print(x, end=' ')
    print()