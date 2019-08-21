T = int(input())
for i in range(T):
    data = list(input())
    stack = []
    top = -1
    flag = 0
    for word in data:
        if word == '(':
            stack.append(word)
            top += 1
        elif word == ')':
            top -= 1
            if top < -1:
                print(f'{i+1} 0')
                flag = 1
            else:
                stack.pop()
        if word == '{':
            stack.append(word)
            top += 1
        elif word == '}':
            top -= 1
            if top < -1:
                print(f'{i+1} 0')
                flag = 1
            else:
                stack.pop()
    if top != -1 and not flag:
        print(f'{i+1} 0')
    elif top == -1 and not flag:
        print(f'{i+1} 1')