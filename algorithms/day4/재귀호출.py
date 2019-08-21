# 재귀 호출
# 1. 재귀적으로 문제를 해결
#   - 재귀적 정의를 코드 구현할 떄
#   - 좀 더 작은 문제의 해를 이용해서 좀 더 큰 문제의 해를 구하는 방법
#   -> 분할 정복, DP
# 2. 그래프 탐색(DFS)
# 3. 백트래킹(상태 공간 트리 탐색)

# for, while를 사용하지 않고 반복

# def printHello(i):
#     if i < 3:
#         print('Hello')
#         printHello(i + 1)

# printHello(0)

# def printHello(i):
#     if i == 3:
#         return 
#     else:
#         print(i, 'Hello')
#         printHello(i + 1)
#         print(i, 'Hello')


# def printHello(i, n):
#     if i == n:
#         return 
#     else:
#         print(i, 'Hello')
#         printHello(i + 1, n)
#         print(i, 'Hello')

# printHello(0,3)


# cnt = 0
# def printHello(i, n):
#     global cnt
#     if i == n:
#         cnt += 1
#         return 
#     else:
#         printHello(i + 1, n) # 1 ** 3
#         printHello(i + 1, n) # 2 ** 3
#         printHello(i + 1, n) # 3 ** 3

# printHello(0,3)
# print('cnt =',cnt)


# 백트래킹
# cnt = 0
# bits =[0] * 3
# def printHello(i, n):
#     global cnt
#     if i == n:
#         cnt += 1
#         print(bits)
#         return 
#     else:
#         bits[i] = 1; printHello(i + 1, n) # 1 ** 3
#         bits[i] = 0; printHello(i + 1, n) # 2 ** 3

# printHello(0,3)
# print('cnt =',cnt)


def fact(n): # n = 문제를 식별하는 값, 문제의 크기
    if n == 0 or n == 1:
        return 1
    
    return fact(n-1) * n

memo = [-1] * 101

def fibo(n):
    if n == 0 or n == 1:
        return n
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

print(fibo(40))

