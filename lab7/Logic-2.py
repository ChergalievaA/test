#1
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small
print(make_bricks(3, 1, 8))
#2
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c
print(lone_sum(1, 2, 3))
#3
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c
print(lucky_sum(1, 2, 3))
#4
def fix_teen(n):
    return 0 if (n >= 13 and n <= 19 and n != 15 and n != 16) else n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
print(no_teen_sum(1, 2, 3)) 
#5
def round10(num):
    return (num + 5) // 10 * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
print(round_sum(16, 17, 18)) 
#6
def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    def is_far(x, y, z):
        return abs(x - y) >= 2 and abs(x - z) >= 2
    
    if is_close(b, a) and is_far(c, a, b):
        return True
    if is_close(c, a) and is_far(b, a, c):
        return True
    return False
print(close_far(1, 2, 10))
#7
def make_chocolate(small, big, goal):
    big_count = min(big, goal // 5)
    remaining = goal - big_count * 5
    if small >= remaining:
        return remaining
    return -1
print(make_chocolate(4, 1, 9))  

