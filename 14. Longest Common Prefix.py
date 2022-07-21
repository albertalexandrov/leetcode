"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""

Explanation: There is no common prefix among the input strings.

"""
import os.path


class Solution1:
    """Решение 1

    Простое решение - использовать готовую функцию.  В повседневной работа применил бы это решение
    Но видимо не такое решение ожидается на собеседованиях по алгоритмам :)

    """
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


solution1 = Solution1()

assert solution1.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
assert solution1.longestCommonPrefix(['dog', 'racecar', 'car']) == ''


class Solution2:
    """Решение 2

    Алгоритм заключается в том, чтобы найти в последовательности strs самое короткое слово -
    очевидно, что общий префикс не будет длиннее самого короткого слова.  Затем пройтись по каждому
    символу этого слова и сравнить с соответствующими символами в других строках

    """
    def longestCommonPrefix(self, strs):
        strs = list(sorted(strs, key=len))
        shortest = strs[0]
        len_ = 0

        for i in range(len(shortest)):
            symbol = shortest[i]
            the_same = True

            for str_ in strs:
                if str_[len_] != symbol:
                    the_same = False
                    break

            if not the_same:
                break

            len_ += 1

        return shortest[:len_]


solution2 = Solution2()

assert solution2.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
assert solution2.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
