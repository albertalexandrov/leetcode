"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

"""


class Solution1:
    """Решение 1.

    Time: O(n)
    Space: O(n)

    Подсмотрено

    Идея заключается в том, чтобы складывать произведение предыдущих чисел на позицию вперед
    При этом конечно не забыть про произведение, которое заканчивается первым элементом

    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        # prefix хранит произведение предыдущих элементов при проходе направо
        # и вставляется в текущую позицию
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # postfix хранит произведение предыдущих элементов при проходе налево
        # и вставляется в текущую позицию
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


s = Solution1()

assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
