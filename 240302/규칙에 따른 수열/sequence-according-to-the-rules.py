def sequence(n):
    if n == 0:
        return 1
    else:
        t = [1]
        for i in range(1, n+1):
            total = 0
            for j in range(i):
                total += t[j] * t[i-j-1]
            t.append(total)
        return t[n]

print(sequence(int(input())))