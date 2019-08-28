def BFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    visit = [[False]*N for _ in range(N)]
    q.append((x, y))
    visit[x][y] = True

    while q:
        cx, cy = q.pop(0)
        if board[cx][cy] == 3:
            return 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx <= N-1 and 0 <= ny <= N-1 and not visit[nx][ny]) and (board[nx][ny] == 0 or board[nx][ny] == 3):
                q.append((nx, ny))
                visit[nx][ny] = True
    return 0


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                print(BFS(i, j))