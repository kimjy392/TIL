# V, E = map(int, input().split()) # 정점수, 간선수
# G = [[] for _ in range(V)]
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     G[u].append(((v, w)))
#     G[v].append((u, w))
#
# pi = [0] * V
# key = [0xffffffff] * V
# visit = [False] * V         # 트리의 포함된 정점과 아닌 정점을 구분하기 위해
#
# key[0] = 0
# cnt = V
# while cnt:      # 모든 정점을 선택할때 까지
#     # 아직 트리에 포함되지 않은 정정들 중에서(visit[x] = False) key 값이 최소인 정점을 찾는다.
#     u, MIN = 0, 0xfffff
#     for i in range(V):
#         if not visit[i] and MIN > key[i]: u, MIN = i, key[i]
#     visit[u] = True
#
#     for v, w in G[u]:
#         if not visit[v] and w < key[v]:
#             key[v] = w
#             pi[v] = u
#     cnt -= 1
#
#     print(pi, key)
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

key = [0xfffff] * V      # 0 ~ V-1
pi = [0] * V
key[0] = 0

cnt = V
visit = [False] * V
while cnt:
    u = MIN = 0xffffff
    for i in range(V):
        if not visit[i] and MIN > key[i]:
            u, MIN = i, key[i]
    visit[u] = True

    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v], pi[v] = w, u

    cnt -= 1


for i in range(V):
    print(i, pi[i], key[i])
