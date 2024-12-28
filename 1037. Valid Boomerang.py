"""
https://leetcode.com/problems/valid-boomerang/description/

Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane,
return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
    Input: points = [[1,1],[2,3],[3,2]]
    Output: true

Example 2:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: false

"""


class Solution:
    def isBoomerang(self, points) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        square = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        return bool(square)


solution = Solution()

assert solution.isBoomerang([[1, 1], [2, 3], [3, 2]]) is True
assert solution.isBoomerang([[1, 1], [2, 2], [3, 3]]) is False
