S = [0] * 3
top = -1

def push(item):
    global top
    # full-상태에 주의 if top == 마지막 인덱스: 파이썬은 괜찮데
    top += 1
    S[top] = item

def pop():
    # empty-상태를 체크
    global top
    if top == -1: return
    ret = S[top]
    top -= 1
    return ret

S.append(1) # push
S.pop() # pop