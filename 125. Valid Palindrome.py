"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_idx, right_idx = 0, len(s) - 1

        while left_idx < right_idx:
            left = s[left_idx].lower()

            while left_idx < right_idx and not left.isalnum():
                left_idx += 1

            right = s[right_idx].lower()

            while left_idx < right_idx and not right.isalnum():
                right_idx -= 1

            print(left, right)

            if left != right:
                return False

            left_idx += 1
            right_idx -= 1

        return True


s = Solution()

assert s.isPalindrome('A man, a plan, a canal: Panama') is True
assert s.isPalindrome('race a car') is False
# assert s.isPalindrome(' ') is True
