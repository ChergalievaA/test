#1
def check_weirdness(n):
    if n % 2 == 1:                          
        print("Weird")
    else:
        if 2 <= n <= 5:                     
            print("Not Weird")
        elif 6 <= n <= 20:               
            print("Weird")
        else:                               
            print("Not Weird")

n = int(input())
check_weirdness(n)
#2
a = int(input())
b = int(input())
sum_ab = a + b
difference_ab = a - b
product_ab = a * b
print(sum_ab)
print(difference_ab)
print(product_ab)
#3
a = int(input())
b = int(input())
print(a // b)
print(a / b)
#4
n = int(input())
for i in range(n):
    print(i ** 2)
#5
n = int(input())
for i in range(1, n + 1):
    print(i, end="")
#6
if __name__ == '__main__':
    N = int(input())  
    my_list = []
    for _ in range(N):
        command = input().split()  
        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            my_list.insert(i, e)
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            my_list.append(e)
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
#7
if __name__ == '__main__':
    n = int(input())  
    integer_list = map(int, input().split()) 
    t = tuple(integer_list)  
    result = hash(t)  
    print(result)  
#8
def split_and_join(line):
    return "-".join(line.split())
if __name__ == "__main__":
    line = input().strip()
    result = split_and_join(line)
    print(result)
#9
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
#10
print("Hello, World!")



