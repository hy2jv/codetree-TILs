a1, a2 = map(int, input().split())
an = [a1, a2]
for i in range(2, 10):
    an.append(an[i-1] + (2*an[i-2]))
print(*an)