
MOD = 10**9 + 7

def matmul(A, B):
    return [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
        ]
    ]

def matpow(A, X):

    result = [[1, 0], [0, 1]]
    while X > 0:
        if X % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        X //= 2
    return result


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a11, a12, a21, a22 = map(int, input().split())
    X = int(input())
    A = [[a11, a12], [a21, a22]]
    AX = matpow(A, X)
    print(AX[0][0], AX[0][1])
    print(AX[1][0], AX[1][1])