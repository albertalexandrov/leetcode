"""
https://leetcode.com/problems/add-digits/

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    Since 2 has only one digit, return it.

Example 2:
    Input: num = 0
    Output: 0

"""


class Solution(object):
    """
    Time: O(1)
    Space: O(1)

    Не сам.  Хз, как можно было бы к такому решению прийти самостоятельно

    """
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 9 == 0:
            return 9

        return num % 9
