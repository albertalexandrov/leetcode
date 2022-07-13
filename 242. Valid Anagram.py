"""
https://leetcode.com/problems/contains-duplicate/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

"""
from collections import Counter


class Solution1(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        return s == t


class Solution2(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


solution = Solution2()

assert solution.isAnagram('anagram', 'nagaram') is True
assert solution.isAnagram('rat', 'car') is False
