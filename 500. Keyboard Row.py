"""
https://leetcode.com/problems/keyboard-row/submissions/

Given an array of strings words, return the words that can be typed using letters of the alphabet
on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
    Input: words = ["Hello","Alaska","Dad","Peace"]
    Output: ["Alaska","Dad"]

Example 2:
    Input: words = ["omk"]
    Output: []

Example 3:
    Input: words = ["adsdf","sfd"]
    Output: ["adsdf","sfd"]

"""


class Solution(object):
    def findWords(self, words):
        rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
        res = []
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(row):
                    res.append(word)
        return res


solution = Solution()

assert solution.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert solution.findWords(["omk"]) == []
assert solution.findWords(["adsdf", "sfd"]) == ["adsdf", "sfd"]
