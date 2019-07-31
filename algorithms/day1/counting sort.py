arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 양의 정수, 최대값을 알아야 된다.
# 최대값 = 4
cnt = [0] * 5 # 배열의 인덱스 n-1 = 4
# 빈도수 계산
for val in arr:
    cnt[val] += 1
print(cnt)
# 누적 빈도수 계산
for i in range(1, len(cnt)):
    cnt[i] = cnt[i - 1] + cnt[i]
print(cnt)

# for val in arr:
#     cnt[val] += 1

# # 누적 빈도수 계산
# numbers = []
# for i in range(len(cnt)):
#     for j in range(cnt[i]):
#         # i가 cnt[i]  반복되는것
#         numbers.append(i)
# print(numbers)

lst = [1, 25, 3, 7, 6, 5, 8, 9, 1]
cnt = [0]*26
for i in lst:
    cnt[i] += 1
numbers = []
for j in range(len(cnt)):
   for num in range(cnt[j]):
       numbers.append(j) 
print(numbers)