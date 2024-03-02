p = []
while True:
    age = int(input())
    if 20 <= age < 30:
        p.append(age)
    else:
        break
print('%0.2f'%(sum(p)/len(p)))