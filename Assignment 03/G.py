import sys
sys.setrecursionlimit(2000)

def build_postorder(pre, pre_start, pre_end, ino, ino_start, ino_end, ino_index, result):
    if pre_start > pre_end or ino_start > ino_end:
        return
    root = pre[pre_start]
    idx = ino_index[root]  
    left_count = idx - ino_start
    build_postorder(pre, pre_start + 1, pre_start + left_count, ino, ino_start, idx - 1, ino_index, result)
    build_postorder(pre, pre_start + left_count + 1, pre_end, ino, idx + 1, ino_end, ino_index, result)
    result.append(root)

N = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))

ino_index = {val: i for i, val in enumerate(in_order)}

result = []
build_postorder(pre_order, 0, N - 1, in_order, 0, N - 1, ino_index, result)
print(*result)