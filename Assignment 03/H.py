
import sys
sys.setrecursionlimit(2000)

def build_preorder(post, post_start, post_end, ino, ino_start, ino_end, ino_index, result):
    if post_start > post_end or ino_start > ino_end:
        return
    root = post[post_end] 
    result.append(root)
    idx = ino_index[root]  
    left_count = idx - ino_start

    build_preorder(post, post_start, post_start + left_count - 1, ino, ino_start, idx - 1, ino_index, result)
    build_preorder(post, post_start + left_count, post_end - 1, ino, idx + 1, ino_end, ino_index, result)

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
ino_index = {val: i for i, val in enumerate(in_order)}

result = []
build_preorder(post_order, 0, N - 1, in_order, 0, N - 1, ino_index, result)
print(*result)