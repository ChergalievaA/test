#1
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return 40 <= cigars <= 60
print(cigar_party(30, False))
#2
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
print(date_fashion(5, 10))
#3
def squirrel_play(temperature, is_summer):
    if is_summer:
        return temperature >= 60 and temperature <= 100
    else:
        return temperature >= 60 and temperature <= 90
print(squirrel_play(70, False)) 
#4
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
print(caught_speeding(60, False))
#5
def sorta_sum(a, b):
    sum_ab = a + b
    if 10 <= sum_ab <= 19:
        return 20
    return sum_ab
print(sorta_sum(3, 4))
#6
def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 6]:  # Weekend
            return 'off'
        else:              # Weekday
            return '10:00'
    else:
        if day in [0, 6]:  # Weekend
            return '10:00'
        else:              # Weekday
            return '7:00'
print(alarm_clock(1, False))
#7
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6
print(love6(6, 4))
#8
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10
print(in1to10(5, False))
#9
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
print(near_ten(12))

