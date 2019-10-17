V, E = map(int, input().split()) # 정점수, 간선수
Edge = [tuple(map(int, input().split())) for _ in range(E)] # (u, v, w)

# disjoin-set
p = [x for x in range(V)]       # 0 ~ V - 1

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])  # path-compression
    return p[x]


Edge.sort(key=lambda x:x[2]) # 가중치 오름차순 정렬
MST = []        # 간선들의 정보를 저장하려고
idx = 0
while len(MST) < V - 1: # V - 1개의 간선을 선택
    u, v, w = Edge[idx]
    a = find_set(u); b = find_set(v)
    if a != b:
        MST.append((u, v, w))
        p[b] = a
    idx += 1

