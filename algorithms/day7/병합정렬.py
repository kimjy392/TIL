arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)

def mergeSort(lo, hi):
    if lo >= hi: return
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)          # 분할쓰 왼쪽
    mergeSort(mid + 1, hi)      # 분할쓰 오른쪽
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]; k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]; k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr[j]; k, j = k + 1, j + 1

    for i in range(lo, hi+1):
        arr[i] = tmp[i]
mergeSort(0, len(arr) - 1)
print(arr)