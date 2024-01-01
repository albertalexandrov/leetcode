"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one
with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and
the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same
row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Example 1:
    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]


Example 2:
    Input: mat = [[1,2],[3,4]], r = 2, c = 4
    Output: [[1,2],[3,4]]

"""


class Solution():
    """
    С данным решением сложно сделать ошибку, оно наглядное, содержит минимальное количество переменных.
    """

    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        flat = [num for row in mat for num in row]

        if len(flat) != r * c:
            return mat

        res = []
        current = 0

        for _ in range(r):
            row = []

            for _ in range(c):
                row.append(flat[current])
                current += 1

            res.append(row)

        return res


solution = Solution()

assert solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
assert solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
assert solution.matrixReshape([[1, 2], [3, 4]], 4, 1) == [[1], [2], [3], [4]]
