#1
def double_char(str):
    result = ''
    for char in str:
        result += char * 2
    return result
print(double_char('The'))  
#2
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == 'hi':
            count += 1
    return count
print(count_hi('abc hi ho')) 
#3
def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 2):
        if str[i:i+3] == 'cat':
            count_cat += 1
        elif str[i:i+3] == 'dog':
            count_dog += 1
    return count_cat == count_dog
print(cat_dog('catdog'))     
#4
def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count
print(count_code('aaacodebbb'))
#5
def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    return a_lower.endswith(b_lower) or b_lower.endswith(a_lower)
print(end_other('Hiabc', 'abc'))  
#6
def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i+3] == 'xyz':
            if i == 0 or s[i-1] != '.':
                return True
    return False
print(xyz_there('abcxyz'))  