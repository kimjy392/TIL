arr = [55, 7, 78, 12, 42]

n = len(arr)

# for i in range(n-1):  # n - 1 ~ 1
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
# for i in range(n-2): # n - 1 ~ 1
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# for i in range(n-3): # n - 1 ~ 1
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]

for j in range(n-1, 0, -1):
    for i in range(j): # n - 1 ~ 1
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)