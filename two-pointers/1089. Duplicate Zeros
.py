"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""
from typing import List

arr =     [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
class Solution:
    def replaceItems(self, arr, i):
        for j in range(len(arr)-1, i, -1):
            arr[j] = arr[j-1]

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)):
            if arr[i] ==0:
                self.replaceItems(arr, i)
            # arr[i] = 0
        print(arr)

sol = Solution()
sol.duplicateZeros(arr)
        