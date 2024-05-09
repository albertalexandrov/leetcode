"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1

"""
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        counter = Counter(s)
        for idx, item in enumerate(s):
            if counter[item] == 1:
                return idx
        return -1


solution = Solution()
assert solution.firstUniqChar("leetcode") == 0
assert solution.firstUniqChar("loveleetcode") == 2
assert solution.firstUniqChar("aabb") == -1
