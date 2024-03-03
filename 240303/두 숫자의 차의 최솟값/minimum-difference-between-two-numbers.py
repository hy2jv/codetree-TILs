n = int(input())
arr = list(map(int, input().split()))
result = max(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        result = min(result, arr[j]-arr[i])
print(result)