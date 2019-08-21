import sys; sys.stdin = open('input.txt', 'r')

def ladder(py, x, y):
    if x == 0:
        return y
    if y != 99 and data[x][y+1] and y + 1 != py:
        return ladder(y, x, y+1)
    elif y != 0 and data[x][y-1] and y - 1 != py:
        return ladder(y, x, y-1)
    else:
        return ladder(y, x-1, y)



for _ in range(1, 11):
    T = int(input())
    x, y = 0, 0
    data = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if data[99][j] == 2:
            x, y = 99, j
    print(f'#{T} {ladder(0, 99, y)}')