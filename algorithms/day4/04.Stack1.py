import sys; sys.stdin = open('input.txt', 'r')
def ladder(px, py):
        while 1:
            while data[px][py]:
                if px == 0:
                    return py
                if py == 99:
                    while data[px][py]:
                        py -= 1
                    py += 1

                elif py == 0:
                    while data[px][py]:
                        py += 1
                    py -= 1
                else:
                    if data[px][py+1]:
                        while data[px][py+1]:
                            py += 1
                            if py == 99:
                                break
                    elif data[px][py-1]:
                        while data[px][py-1]:
                            py -= 1
                            if py == 0:
                                break
                            
                px -= 1


for _ in range(1, 11):
    T = int(input())
    x, y = 0, 0
    data = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if data[99][j] == 2:
            x, y = 99, j
    print(f'#{T} {ladder(x, y)}')