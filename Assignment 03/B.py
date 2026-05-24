
import bisect

n = int(input())
A = list(map(int, input().split()))

count = 0
seen_squares = []

for i in range(n - 1, -1, -1):
    idx = bisect.bisect_left(seen_squares, A[i])
    count += idx
    bisect.insort(seen_squares, A[i] ** 2)

print(count)