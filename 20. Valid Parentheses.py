"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

"""


class Solution(object):
    def isValid(self, s):
        brackets = {'}': '{', ')': '(', ']': '['}
        stack = []

        for bracket in s:
            if bracket in brackets:
                if not stack or stack.pop() != brackets[bracket]:
                    return False
            else:
                stack.append(bracket)

        return not stack


solution = Solution()

assert solution.isValid('()') is True
assert solution.isValid('()[]{}') is True
assert solution.isValid('(]') is False
assert solution.isValid('((') is False
assert solution.isValid('[') is False
assert solution.isValid('}') is False
assert solution.isValid(')(){}') is False
