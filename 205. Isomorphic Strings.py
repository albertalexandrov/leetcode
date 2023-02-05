"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))


solution = Solution()

assert solution.isIsomorphic('egg', 'add') is True
assert solution.isIsomorphic('foo', 'bar') is False
assert solution.isIsomorphic('paper', 'title') is True
assert solution.isIsomorphic('badc', 'baba') is False
