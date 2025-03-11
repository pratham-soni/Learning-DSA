"""
ou have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

 

Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5



"""

from typing import List
nums = [7,8,3,4,15,13,4,1]

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # left, right = 0, len(nums)-1
        # avg = float('inf')
        # nums.sort()
        # while left < right:
        #     temp = (nums[left]+nums[right])/2
        #     avg = temp if avg > temp else avg
        #     left +=1
        #     right -=1
        # return avg
        nums.sort()
        return min((nums[i] + nums[~i]) / 2 for i in range(len(nums)//2))
    
sol = Solution()
print(sol.minimumAverage(nums))