"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


"""


class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words) != len(pattern):
            return False
        word_to_char = {}
        char_to_word = {}
        for word, char in zip(words, pattern):
            if word in word_to_char and word_to_char[word] != char:
                return False
            if char in char_to_word and char_to_word[char] != word:
                return False
            word_to_char[word] = char
            char_to_word[char] = word
        return True


solution = Solution()
assert solution.wordPattern("abba", "dog cat cat dog") is True
assert solution.wordPattern("abba", "dog dog dog dog") is False
assert solution.wordPattern("aaa", "aa aa aa aa") is False
