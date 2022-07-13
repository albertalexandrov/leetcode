"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from pympler.asizeof import asizeof


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        answer = 0
        lookups = {}
        start = 0

        for i, num in enumerate(s):
            if num in lookups:
                start = max(lookups[num] + 1, start)
            answer = max(answer, i - start + 1)
            lookups[num] = i

        return answer


s = Solution()
s.lengthOfLongestSubstring('abcadbjfdcklskvfgjnmcpcwfwvefnmsdkcvnsdsdjceorivdfjhcnsklmbcbb'*1000)
# assert s.lengthOfLongestSubstring('bbbbb') == 1
# assert s.lengthOfLongestSubstring('pwwkew') == 3
# assert s.lengthOfLongestSubstring('au') == 2
# assert s.lengthOfLongestSubstring('dvdf') == 3
# assert s.lengthOfLongestSubstring('') == 0
# assert s.lengthOfLongestSubstring('abba') == 2


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = right = 0

        res = 0

        while right < len(s):
            symbol = s[right]
            index: int | None = chars[ord(symbol)]

            if index is not None and index >= left:
                left = index + 1

            res = max(res, right - left + 1)
            chars[ord(symbol)] = right
            right += 1

        print(asizeof(chars))

        return res


s = Solution()
assert s.lengthOfLongestSubstring('abba') == 2
