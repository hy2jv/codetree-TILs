def func(x, y):
    if y == 1:
        return x
    else:
        return x * func(x, y-1)

a, b = map(int, input().split())
print(func(a, b))