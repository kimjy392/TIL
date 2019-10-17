# 트리
# 13, 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V, E = map(int, input().split()) # 노드수, 간선수
L = [0] * (V + 1)   # tree = [[0, 0, 0] for _ in range(V + 1)]
R = [0] * (V + 1)   # tree = [[] for _ range(V + 1)]
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i+1]
    if L[arr[i]] == 0: L[p] = c
    else: R[p] = c
    P[c] = p    # 부모 정보는 필요한 경우에 저장해서 사용
#-------------------------------------
def inorder(v):
    if v == 0: return
    print(v, end= ' ') # 전위 순회
    inorder(L[v])
    print(v, end=' ') # 중위 순회
    inorder(R[v])
    print(v, end=' ') # 후위 순회

    # if L[v]:
    #     inorder(L[v])
    # if R[v]:
    #     inorder(R[v])

#-------------------------------------
inorder(1)
