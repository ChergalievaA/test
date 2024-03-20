#a
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")
#b
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    if i % d == c:
        print(i)
#c
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i == (int(i ** 0.5) ** 2):
        print(i)
#d
x = input()
d = input()
count = 0
for digit in x:
    if digit == d:
        count += 1
print(count)
#e
x = input()
sum = 0
for d in x:
    sum += int(d)
print(sum)
#f
x = int(input())
x_str = str(x)
reversed_x = ""
for i in range(len(x_str) - 1, -1, -1):
    reversed_x += x_str[i]
reversed_x = int(reversed_x)
print(reversed_x)
#g
x = int(input())
for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break
#h
x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
     print(i)
#i
x = int(input())
count = 0
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
        count += 1
        if i != x // i:
            count += 1
print(count)
#j
total_sum = 0
for _ in range(100):
    number = int(input())
    total_sum += number
print(total_sum)
#k
N = int(input())
total_sum = 0
for _ in range(N):
    number = int(input())
    total_sum += number
print(total_sum)
#l
b = input()
d = 0
for i in range(len(b)):
 d+= int(b[i]) * 2 ** (len(b) - i - 1)
print(d)
#m
N = int(input())
count = 0
for _ in range(N):
    number = int(input())
    if number == 0:
        count += 1
print(count)
