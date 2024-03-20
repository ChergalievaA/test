#a
N = int(input())
array = list(map(int, input().split()))
for i in range(0, N, 2):
    print(array[i], end=' ')
#b
N = int(input())
array = list(map(int, input().split()))
for num in array:
    if num % 2 == 0:
        print(num, end=' ')
#c
N = int(input())
array = list(map(int, input().split()))
count_positive = 0
for num in array:
    if num > 0:
        count_positive += 1
print(count_positive)
#d
N = int(input())
array = list(map(int, input().split()))
count = 0
for i in range(1, N):
    if array[i] > array[i - 1]:
        count += 1
print(count)
#e
N = int(input())
array = list(map(int, input().split()))
found = False
for i in range(1, N):
    if array[i] * array[i - 1] > 0:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")
#f
N = int(input())
array = list(map(int, input().split()))
count = 0
for i in range(1, N - 1):
 if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1
print(count)
#g
N = int(input())
array = list(map(int, input().split()))
for i in range(N // 2):
    array[i], array[N - i - 1] = array[N - i - 1], array[i]
for num in array:
    print(num, end=' ')

