"""
https://leetcode.com/problems/flipping-an-image/description/

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

Example 1:
    Input: image = [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:
    Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

"""


class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            for i in range((len(row) + 1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image


solution = Solution()

assert solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
assert solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == [[1, 1, 0, 0],
                                                                                                 [0, 1, 1, 0],
                                                                                                 [0, 0, 0, 1],
                                                                                                 [1, 0, 1, 0]]
