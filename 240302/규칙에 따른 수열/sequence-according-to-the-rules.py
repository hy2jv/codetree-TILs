n = int(input())
arr = [0] * (n+1)
arr[0] = 1
arr[1] = 1
arr[2] = 2
for idx in range(3, n+1):
    result = 0
    for i in range(n):
        result += (arr[i] * arr[n-i-1])
    arr[idx] = result
print(arr[n])