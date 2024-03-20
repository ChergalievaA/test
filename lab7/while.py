#a
N = int(input())
number = 1
while number ** 2 <= N:
    print(number ** 2)
    number += 1
#b
n = int(input())
d = 2
while n % d != 0:
    d += 1
print(d)
#c
N = int(input())
power = 1
while power <= N:
    print(power, end=' ')
    power *= 2
#d
N = int(input())
while N > 1 and N % 2 == 0:
    N //= 2
if N == 1:
    print("YES")
else:
    print("NO")
#e
N = int(input())
power = 0
while 2 ** power < N:
    power += 1
print(power)

