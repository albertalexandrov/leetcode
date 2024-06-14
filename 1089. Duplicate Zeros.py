"""
https://leetcode.com/problems/duplicate-zeros/

Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

"""


class Solution(object):
    def duplicateZeros(self, arr):
        result = []
        for num in arr:
            result.append(num)
            if len(result) == len(arr):
                break
            if num == 0 and len(result) != len(arr):
                result.append(num)
        return result


solution = Solution()

assert solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4]
assert solution.duplicateZeros([8, 5, 0, 9, 0, 3, 4, 7]) == [8, 5, 0, 0, 9, 0, 0, 3]
assert solution.duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7]) == [8, 4, 5, 0, 0, 0, 0, 0]
assert solution.duplicateZeros([1, 2, 3]) == [1, 2, 3]
