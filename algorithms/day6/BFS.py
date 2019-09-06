from collections import deque

def BFS(s, G):      # s=시작점
    # 큐를 생성
    Q = []
    visit = [False] * (V + 1)
    visit[s] = True; print(s)   # 방문표시
    Q.append(s)                 # 시작점을 방문하고 큐에 삽입
    while Q:       # 빈큐가 될 때까지
        v = Q.pop(0)    # 방문한 정점을 빼서
        for w in G[v]:  # 인접한 정점들을 불러서
            if not visit[w]:    # 방문하지 않았다면,
                visit[w] = True; print(w)   # 방문하자
                Q.append(w) # 방문한 곳을 큐에 넣어줘
# ----------------------------------------------
# 최단거리구하기
# D[]: 최단거리를 저장, P[]: 최단경로트리
def BFS_1(s, G)
    Q = []
    D[s], P[s] = 0, s
    visit = [False] * (V + 1)
    visit[s] = True; print(s)   # 방문표시
    Q.append(s)                 # 시작점을 방문하고 큐에 삽입
    while Q:       # 빈큐가 될 때까지
        v = Q.pop(0)    # 방문한 정점을 빼서
        for w in G[v]:  # 인접한 정점들을 불러서
            if not visit[w]:    # 방문하지 않았다면,
                visit[w] = True; print(w)   # 방문하자
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w) # 방문한 곳을 큐에 넣어줘
# 정접의 정보와 같이 거리를 저장해도 되고
# ----------------------------------------------
import sys
sys.stdin = open("BFS_input.txt", "r")


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
D = [0] * (V + 1) # 최단 거리를 저장
P = [0] * (V + 1) # 최단 경로 트리
for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
BFS(1, G)

# print(D[1:])