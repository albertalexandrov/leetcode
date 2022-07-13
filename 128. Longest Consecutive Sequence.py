"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                longest = max(length, longest)

        return longest


"""
решение которое в 10 раз быстрее верхнего и потребляющее меньше памяти, но по скорости не О(n):

class Solution:
    def longestConsecutive(self, nums):
        nums = sorted(nums)
        
        if len(nums) == 0:
            return 0
        
        lcs = 1
        temp = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
                
            if nums[i-1]+1 == nums[i]:
                temp += 1
            else:
                temp = 1
                
            if temp > lcs:
                lcs = temp
                
        return lcs
        
"""


s = Solution()

assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
