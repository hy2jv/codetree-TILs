n = int(input())
count = 1
for i in range(n):
    x = (n*(i+1))
    for _ in range(n):
        print(x, end=' ')
        x -= count
    count += 1
    print()