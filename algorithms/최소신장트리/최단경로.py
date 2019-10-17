from collections import deque

def BFS(s):
    D = [0xffffffff] * (V + 1)      # D[] 초기값 설정!!!!!
    P = [0] * (V+1)
    # visit = [False] * (V + 1)
    Q = deque()
    Q.append(s); D[s] = 0

    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:            # u ----> v
                D[v] = D[u] + w
                Q.append(v)
                P[u] = v

V , E = map(int, input().split())  # 정점수, 간선수
G = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append(((v, w)))
    G[v].append((u, w))
BFS(1)
