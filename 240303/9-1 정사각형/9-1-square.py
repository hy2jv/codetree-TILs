n = int(input())
x = 9
for _ in range(n):
    for _ in range(n):
        print(x, end='')
        if x > 1:
            x -= 1
        else:
            x = 9
    print()