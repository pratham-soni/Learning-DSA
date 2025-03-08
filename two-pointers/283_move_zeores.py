"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

nums = [0,1,0,3,12]
def move_zeores(nums):
    first, second = 0, 0
    for first in range(len(nums)):
        if (nums[first] != 0):
            nums[first], nums[second] = nums[second], nums[first]
            second +=1

move_zeores(nums)
print(nums)
