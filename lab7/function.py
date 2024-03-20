#a
def min_(a, b, c, d):
    return min(a, b, c, d)
a, b, c, d = map(int, input().split())
print(min_(a, b, c, d))
#b
def power(a, n):
    return a ** n
a, n = map(float, input().split())
print(power(a, int(n)))
#c
def xor(x, y):
    return int((x or y) and not (x and y))
x, y = map(int, input().split())
print(xor(x, y))


