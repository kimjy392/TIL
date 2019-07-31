import sys
sys.stdin = open('input(view).txt', 'r')

for i in range(1, 11):
    numbers = int(input())
    house = list(map(int, input().split()))
    count = 0
    for idx in range(2, len(house) - 2):
        if house[idx-2] < house[idx] and house[idx-1] < house[idx] and house[idx+1] < house[idx] and house[idx+2] < house[idx]:
            max_num = 0
            for j in (house[idx-2], house[idx-1], house[idx+1], house[idx+2]):
                if max_num < j:
                    max_num = j
            count += house[idx] - max_num
    print('#{} {}'.format(i, count))
