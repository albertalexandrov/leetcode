"""
https://leetcode.com/problems/contains-duplicate/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

"""
from collections import Counter


class Solution1:
    """Решение 1.

    Time: O(n)
    Space: O(n)

    Предпочтительное решение из-за простоты кода, его минималистичности и читаемости, в нем сложно ошибиться

    Временная сложность обусловлена преобразованием строк в Counter (2n принимаем за n)
    То же самое и с пространственной сложностью (в худшем случае будет Counter, в котором n элементов)

    """

    def is_anagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


solution1 = Solution1()

assert solution1.is_anagram('anagram', 'nagaram') is True
assert solution1.is_anagram('rat', 'car') is False


class Solution2(object):
    """Решение 2.

    Time: O(nlog(n))
    Space: O(n)

    Решение простое, читаемое, не требует библиотек

    Временная сложность обусловлена сортировкой.  Пространственная сложность обусловлена тем,
    что на строках sorted возвращает список символов

    """
    def is_anagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


solution2 = Solution2()

assert solution2.is_anagram('anagram', 'nagaram') is True
assert solution2.is_anagram('rat', 'car') is False


class Solution3:
    """Решение 3.

    Time: O(nlog(n))
    Space: O(n)

    Временная сложность обусловлена сортировкой.  Пространственная сложность обусловлена
    преобразованием строк в списки

    """
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False

        s, t = list(s), list(t)

        s.sort()
        t.sort()

        return s == t


solution3 = Solution3()

assert solution3.is_anagram('anagram', 'nagaram') is True
assert solution3.is_anagram('rat', 'car') is False
