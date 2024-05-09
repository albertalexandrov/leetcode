"""
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

"""


from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        for letter, count in r_counter.items():
            if m_counter.get(letter, 0) < count:
                return False
        return True


solution = Solution()
assert solution.canConstruct("a", "b") is False
assert solution.canConstruct("aa", "ab") is False
assert solution.canConstruct("aa", "aab") is True
