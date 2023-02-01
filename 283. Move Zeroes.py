"""
https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

"""


class Solution1(object):
    """Решение 1 - Метод двух указателей

    Time: O(n)
    Space: O(1)

    i - указатель на текущий элемент в списке
    j - указатель на первый ноль, с которым меняется местами ненулевой элемент

    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

        return nums


solution1 = Solution1()

assert solution1.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert solution1.moveZeroes([0]) == [0]


class Solution2(object):
    """Решение 2

    Time: O(n)
    Space: O(1)

    Сначала влево сдвигаются все ненулевые элементы, а потом начиная с первой после последнего
    ненулевого элемента на позиции ставятся нули

    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0

        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0

        return nums


solution2 = Solution2()

assert solution2.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert solution2.moveZeroes([0]) == [0]
