"""
https://leetcode.com/problems/find-the-difference/

You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:
    Input: s = "abcd", t = "abcde"
    Output: "e"
    Explanation: 'e' is the letter that was added.

Example 2:
    Input: s = "", t = "y"
    Output: "y"

"""


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def findTheDifference(self, s, t):
        runsum = 0

        for i in t:
            runsum += ord(i)

        for i in s:
            runsum -= ord(i)

        return chr(runsum)


solution = Solution()
solution.findTheDifference('abcd', 'abcde')
