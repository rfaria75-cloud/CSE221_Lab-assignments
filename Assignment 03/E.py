
import sys
input = sys.stdin.readline

def mod_pow_sum(a, n, m):
    if n == 0:
        return (1, 0)
    if n == 1:
        return (a % m, a % m)
    
    power, summation = 1, 0
    res_pow, res_sum = 1, 0
    base_pow, base_sum = a % m, a % m
    while n > 0:
        if n & 1:
            res_sum = (res_sum * base_pow + base_sum) % m
            res_pow = (res_pow * base_pow) % m
        base_sum = (base_sum * (1 + base_pow)) % m
        base_pow = (base_pow * base_pow) % m
        n >>= 1
    return (res_pow, res_sum)

T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    if a == 1:
        print(n % m)
    else:
        _, total = mod_pow_sum(a, n, m)
        print(total % m)