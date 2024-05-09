"""
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""


from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        counter = Counter(s)
        res = 0
        for letter, count in list(counter.items()):
            if count % 2 == 0:
                res += count
                counter.pop(letter)
            else:
                res += count - 1
        if counter:
            return res + 1
        return res


solution = Solution()
assert solution.longestPalindrome("abccccdd") == 7
assert solution.longestPalindrome("a") == 1
