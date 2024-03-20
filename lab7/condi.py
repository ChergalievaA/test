#a
a = int(input())
b = int(input())
max_number = max(a, b)
print(max_number)
#b
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
#c
test_system_answer = int(input())
student_answer = int(input())
if test_system_answer == 1 and student_answer == 1:
    print("YES")
elif test_system_answer != 1 and student_answer != 1:
    print("YES")
else:
    print("NO")
#e
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
