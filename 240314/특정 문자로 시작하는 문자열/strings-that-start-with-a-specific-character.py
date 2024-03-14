n = int(input())
arr = []
for i in range(n):
    arr.append(input())
searchChar = input()
cnt, result = 0, 9
for i in range(n):
    if searchChar in arr[i]:
        cnt += arr[i].count(searchChar)
        result += len(arr[i])
print('%d %.2f' % (cnt, round(result/cnt, 2)))