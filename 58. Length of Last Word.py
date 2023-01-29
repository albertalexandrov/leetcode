"""
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.

Example 3:
    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.

"""


class Solution1(object):
    def lengthOfLastWord(self, s):
        """Решение 1.

        Я бы выбрал это решение несмотря на бОльшую пространственную сложность (создается список)
        по сравнению с решением 2.  Оно простое и сходу понятное.  Ошибиться сложно

        Time: O(n)
        Space: O(n)

        """
        s = s.strip()
        last_word = s.split()[-1]

        return len(last_word)


solution = Solution1()

assert solution.lengthOfLastWord('Hello World') == 5
assert solution.lengthOfLastWord('   fly me   to   the moon  ') == 4
assert solution.lengthOfLastWord('luffy is still joyboy') == 6


class Solution2(object):
    def lengthOfLastWord(self, s):
        """Решение 2.

        Time: O(n)
        Space: O(1)

        Итерируемся с конца, так как нужно найти длину последнего слова, чтобы не итерироваться лишнего

        """
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                while s[i] != ' ' and i >= 0:
                    length += 1
                    i -= 1
                break

        return length


solution2 = Solution2()

assert solution2.lengthOfLastWord('Hello World') == 5
assert solution2.lengthOfLastWord('   fly me   to   the moon  ') == 4
assert solution2.lengthOfLastWord('luffy is still joyboy') == 6
assert solution2.lengthOfLastWord('a') == 1
