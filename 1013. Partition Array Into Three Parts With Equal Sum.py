"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i]
== arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
    Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
    Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false

Example 3:
    Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

"""


class Solution(object):
    """

    Time: O(n)
    Space: O(1)

    Notes:
        Поначалу не сообразил, что ввиду того, что отрезки должны иметь одинаковую сумму,
        нужно получить сумму всех элементов и поделить на 3, чтобы узнать, какая должна
        быть сумма (target) каждого отрезка и от нее отталкиваться

    """

    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        target, remainder = divmod(sum(arr), 3)

        if remainder != 0:
            return False

        cumsum, parts = 0, 0

        for i in range(len(arr)):
            cumsum += arr[i]

            if cumsum == target:
                parts += 1
                cumsum = 0

        return parts >= 3


solution = Solution()

assert solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) is True
assert solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) is False
assert solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) is True
assert solution.canThreePartsEqualSum([0, 0, 0, 0]) is True
