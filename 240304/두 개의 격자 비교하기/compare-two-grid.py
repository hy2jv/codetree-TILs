n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
brr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == brr[i][j]:
            print(0, end =' ')
        else:
            print(1, end=' ')
    print()