# # 중복순열
# arr = "ABC"
# n = len(arr)
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(arr[i], arr[j], arr[k])
arr = 'ABC'
# 중복 x
n = len(arr)
for i in range(n):
    for j in range(n):
        if j == i: continue
        for k in range(n):
            if k == j or k == i: continue
            print(arr[i], arr[j], arr[k])

