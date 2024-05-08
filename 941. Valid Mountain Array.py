"""
https://leetcode.com/problems/valid-mountain-array/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

"""


class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        i, j = 0, len(arr) - 1
        while i < j and arr[i] < arr[i + 1]:
            i += 1
        if i == 0:
            return False
        while j > i and arr[j - 1] > arr[j]:
            j -= 1
        if j == len(arr) - 1:
            return False
        return i == j


solution = Solution()

assert solution.validMountainArray([2, 1]) is False
assert solution.validMountainArray([3, 5, 5]) is False
assert solution.validMountainArray([0, 3, 2, 1]) is True
