#1
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
print(count_evens([2, 1, 2, 3, 4])) 
#2
def big_diff(nums):
    return max(nums) - min(nums)
print(big_diff([10, 3, 5, 6])) 
#3
def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)
print(centered_average([1, 2, 3, 4, 100])) 
#4
def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2  # Skip the number after 13
            continue
        total += nums[i]
        i += 1
    return total
print(sum13([1, 2, 2, 1])) 
#5
def sum67(nums):
    total = 0
    ignore_section = False
    for num in nums:
        if num == 6:
            ignore_section = True
        if not ignore_section:
            total += num
        if num == 7:
            ignore_section = False
    return total
print(sum67([1, 2, 2]))
#6
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
print(has22([1, 2, 2]))  