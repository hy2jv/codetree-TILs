from collections import deque

q = deque()
for _ in range(int(input())):
    command = input().split()
    if (command[0] == 'push'):
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if len(q) == 0: print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif command[0] == 'front':
        if len(q) == 0: print(-1)
        else: 
            x = q.popleft()
            print(x)
            q.appendleft(x)
    elif command[0] == 'back':
        if len(q) == 0: print(-1)
        else:
            x = q.pop()
            print(x)
            q.append(x)