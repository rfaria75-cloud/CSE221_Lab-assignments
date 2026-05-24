
def merge(a,b):
    i = 0
    j = 0
    merged = []
    inv_count = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            inv_count += len(a) - i
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, inv_count
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merge_inv = merge(left, right)
    total_inv = left_inv + right_inv + merge_inv
    return merged, total_inv
n=int(input())
arr=list(map(int,input().split()))
sorted_arr, inv_count = merge_sort(arr)
print(inv_count)
print(*sorted_arr)