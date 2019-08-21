T = int(input())
for testcase in range(T):
    data = list(input())
    data_2 = data[:]
    N = len(data)
    for i in range(N//2):
        data_2[i], data_2[N-1-i] = data_2[N-1-i], data_2[i]
    result = 1 if data == data_2 else 0
    print('#{} {}'.format(testcase+1, result))
