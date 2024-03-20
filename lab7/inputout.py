#a
import math
def find_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
a = int(input())
b = int(input())
print(find_hypotenuse(a, b))
#b
number = int(input())
print("The next number for the number", number, "is", number + 1, end=".\n")
print("The previous number for the number", number, "is", number - 1, end=".")
#c
N = int(input())
K = int(input())
apples_per_student = K // N
print(apples_per_student)
#d
N = int(input())
K = int(input())
apples_left = K % N
print(apples_left)
#e
v = int(input())
t = int(input())
position = (0 + v * t) % 109
print(position)
