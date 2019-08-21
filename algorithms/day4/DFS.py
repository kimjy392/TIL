import sys; sys.stdin = open('04 Stack1_DFS_input.txt', 'r')

def DFS(v):
    # 시작점을 방문하고, 스택에 push
    S = []
    visit[v] = True; print(v, end=' ') 
    S.append(v)
    while S:                    # 빈스택이 아닐동안 반복
        for w in G[v]:
            if not visit[w]:    # v의 방문하지 않은 인접정점을 w에 찾아서
                visit[w] = True; print(w, end=' ') # w를 방문하고,
                S.append(v)     # v를 스택에 push
                v = w           # v를 w로 설정
                break
        else:                   # 인접정점이 없다면, 스택에서 pop()해서
            v = S.pop()         # v로 설정

def DFS_1(v): # v = 현재 방문하는 정점
    visit[v] = True; print(v, end=' ') 
    for w in G[v]:
        if not visit[w]:    # v의 방문하지 않은 인접정점을 w에 찾아서
            DFS_1(w)
        

V, E = map(int, input().split()) # 정점수, 간선수
print(V, E)
G = [[] for _ in range(V + 1)] # 1 ~ V 까지 0번을 안쓰고 비워두는거에요 여기서는 안쓰니까 나중에 쓰면 쓰는거고
visit = [False] * (V + 1)       # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)          # 무향 그래프

for i in range(1, V + 1):
    print(i, '-->', G[i])

DFS(1)
DFS_1(1)