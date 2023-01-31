"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""


class Solution(object):
    """Решение

    Time: O(n)
    Space: O(1)

    Notes:
        Можно заморочиться и реализовать при помощи бинарного поиска

    """
    def mySqrt(self, x):
        result = 1

        while result * result <= x:
            result += 1

        return result - 1


solution = Solution()

assert solution.mySqrt(4) == 2
assert solution.mySqrt(8) == 2
