'''
    In an array of numbers, only one kind appears odd times. Find it.
'''


def find_odd_times(nums):
    res = 0
    
    for num in nums:
        res ^= num
        
    print(res)
    

if __name__ == '__main__':
    nums = [1, 2, 2, 1, 3, 2, 3]
    find_odd_times(nums)
    
