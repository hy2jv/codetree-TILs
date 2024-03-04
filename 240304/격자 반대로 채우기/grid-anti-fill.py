n = int(input())
arr = [[0] * n for _ in range(n)]
x = 1
for i in range(n-1, -1, -1):
    if i % 2 == 1:
        for j in range(n-1, -1, -1):
            arr[j][i] = x
            x += 1
    else:
        for j in range(n):
            arr[j][i] = x
            x += 1
for i in range(n):
    print(*arr[i])