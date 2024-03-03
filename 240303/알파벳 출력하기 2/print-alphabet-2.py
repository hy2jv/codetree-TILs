n = int(input())
arr = [chr(ord('A')+i) for i in range(26)]
idx = 0
for i in range(n):
    print('  ' * i, end='')
    for j in range(n-i):
        print(arr[idx], end=' ')
        idx += 1
    print()