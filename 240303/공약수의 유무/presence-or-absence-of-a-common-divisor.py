a, b = map(int, input().split())
for i in range(a, b+1):
    if 1920 % i == 0 or 2880 % i == 0:
        result = 1
        break
    else:
        result = 0
print(result)