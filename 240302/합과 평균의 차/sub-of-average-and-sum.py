a, b, c = map(int, input().split())
sumValue = a + b + c
avg = sumValue//3
minus = sumValue - avg
print('%d\n%d\n%d'%(sumValue, avg, minus))