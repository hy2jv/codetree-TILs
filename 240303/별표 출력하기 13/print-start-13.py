n = int(input())
odd, even = 1, n
for i in range(2*n):
    if i % 2 == 0:
        print('* ' * even)
        even -= 1
    else:
        print('* ' * odd)
        odd += 1