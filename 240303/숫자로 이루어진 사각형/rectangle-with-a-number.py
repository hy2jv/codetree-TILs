def rect(n):
    x = 1
    for i in range(n):
        for j in range(n):
            if x == 10: x = 1
            print(x%10, end=" ")
                
            x += 1
        print()
rect(int(input()))