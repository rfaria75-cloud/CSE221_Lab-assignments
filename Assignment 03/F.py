
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = []

stack = [(0, n - 1)]

while stack:
    l, r = stack.pop()
    if l > r:
        continue
    mid = (l + r) // 2
    result.append(arr[mid])
    stack.append((mid + 1, r))
    stack.append((l, mid - 1))

print(*result)