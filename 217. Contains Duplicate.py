"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

"""


class Solution1:
    """Решение 1.

    Time: O(n)
    Space: O(n)

    Предпочтительное благодаря скорости, читаемости и сложно ошибиться

    """

    def contains_duplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True

            hashset.add(num)

        return False


solution1 = Solution1()

assert solution1.contains_duplicate([1, 2, 3, 1]) is True
assert solution1.contains_duplicate([1, 2, 3, 4]) is False
assert solution1.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


class Solution2:
    """Решение 2.

    Time: O(nlog(n))
    Space: O(1)

    Временная сложность обусловлена сортировкой

    """

    def contains_duplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):  # чтобы не получить исключение IndexError на последнем элементе
            if nums[i] == nums[i + 1]:
                return True

        return False


solution2 = Solution2()

assert solution2.contains_duplicate([4, 2, 3, 3]) is True
assert solution2.contains_duplicate([1, 2, 3, 4]) is False


class Solution3:
    """Решение 3.

    Time: O(n^2)
    Space: O(1)

    Временная сложность обусловлена тем, что для каждого элемента (n) приходится проходить весь список (n)

    """

    def contains_duplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


solution3 = Solution3()

assert solution3.contains_duplicate([4, 2, 3, 3]) is True
assert solution3.contains_duplicate([1, 2, 3, 4]) is False
