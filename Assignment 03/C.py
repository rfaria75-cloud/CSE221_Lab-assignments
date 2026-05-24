
def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
n,y=map(int,input().split())
print(pow_mod(n,y,107))