"""https://leetcode.com/problems/height-checker/"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for idx, height in enumerate(sorted(heights)):
            if height != heights[idx]:
                count += 1
        return count
