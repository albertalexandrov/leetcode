"""
https://leetcode.com/problems/reverse-string-ii/

Given a string s and an integer k, reverse the first k characters for every 2k characters counting
from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Example 2:
    Input: s = "abcd", k = 2
    Output: "bacd"

"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        chars = []
        while i < len(s):
            for j in range(min(i + k, len(s)) - 1, i - 1, -1):
                chars.append(s[j])
                i += 1
            for i in range(i, min(i + k, len(s))):
                chars.append(s[i])
            i += 1
        return "".join(chars)


solution = Solution()

assert solution.reverseStr("abcdefg", 2) == "bacdfeg"
assert solution.reverseStr("abcdefg", 3) == "cbadefg"
