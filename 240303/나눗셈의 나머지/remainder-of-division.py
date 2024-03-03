a, b = map(int, input().split())
cnt = [0] * 10
while a > 1:
    cnt[a%b] += 1
    a//=b
result = 0
for i in cnt:
    result += pow(i, 2)
print(result)