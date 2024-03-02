n = int(input())
arr = [0] * (n+1)
arr[0] = 1
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
    result = 0
    for j in range(i+1):
        result += (arr[j] * arr[n-j-1])
    arr[i] = result
print(arr[n])