"""
https://leetcode.com/problems/set-mismatch/

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
due to some error, one of the numbers in s got duplicated to another number in the set, which results
in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
    Input: nums = [1,2,2,4]
    Output: [2,3]

Example 2:
    Input: nums = [1,1]
    Output: [1,2]

"""
from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        repeated = None
        for num, count in counter.items():
            if count == 2:
                repeated = num
                break
        missed = sum(range(1, len(nums) + 1))
        for num in counter.keys():
            missed -= num
        return [repeated, missed]
