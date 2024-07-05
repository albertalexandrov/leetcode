"""
https://leetcode.com/problems/decode-the-message/

You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:
    1. Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    2. Align the substitution table with the regular English alphabet.
    3. Each letter in message is then substituted using the table.
    4. Spaces ' ' are transformed to themselves.

For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

Return the decoded message.

"""

import string


class Solution(object):
    def decodeMessage(self, key, message):
        table, space = {}, " "
        key = (char for char in key if char != space)
        for char in key:
            if char not in table:
                table[char] = string.ascii_lowercase[len(table)]
        res = ""
        for char in message:
            res += space if char == space else table[char]
        return res


solution = Solution()

assert solution.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv") == "this is a secret"
assert solution.decodeMessage(
    "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
) == "the five boxing wizards jump quickly"
