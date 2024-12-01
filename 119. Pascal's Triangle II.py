from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current = prev = [1]
        current_row = 1
        while current_row <= rowIndex:
            current = [1]
            for j in range(1, len(prev)):
                current.append(prev[j] + prev[j - 1])
            current.append(1)
            prev = current
            current_row += 1
        return current


solution = Solution()
assert solution.getRow(3) == [1, 3, 3, 1]
assert solution.getRow(0) == [1]
assert solution.getRow(1) == [1, 1]
