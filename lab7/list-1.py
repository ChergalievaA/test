#1
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6
print(first_last6([1, 2, 6])) 
#2
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]
print(same_first_last([1, 2, 3]))    
print(same_first_last([1, 2, 1]))
#3
def make_pi():
    return [3, 1, 4]
print(make_pi())
#4
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]
print(common_end([1, 2, 3], [7, 3]))    
print(common_end([1, 2, 3], [7, 3, 2])) 
print(common_end([1, 2, 3], [1, 3]))
#5
def sum3(nums):
    return sum(nums)
print(sum3([1, 2, 3])) 
#6
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
print(rotate_left3([1, 2, 3]))
#7
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]
print(reverse3([1, 2, 3])) 
#8
def max_end3(nums):
    max_value = max(nums[0], nums[2])
    return [max_value] * 3
print(max_end3([1, 2, 3])) 
#9
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return sum(nums)
    else:
        return nums[0] + nums[1]
print(sum2([1, 2, 3]))
#10
def middle_way(a, b):
    return [a[1], b[1]]
print(middle_way([1, 2, 3], [4, 5, 6])) 
#11
def make_ends(nums):
    return [nums[0], nums[-1]]
print(make_ends([1, 2, 3]))   
#12
def has23(nums):
    return 2 in nums or 3 in nums
print(has23([2, 5]))
