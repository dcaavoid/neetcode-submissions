class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m > n:
        # 1 2
        # 3 4 
        # 5 6
        # l = 0, r = 1, t = 1, b = 3
        # 1, 2, 4, 6

        # m < n:
        # 1 2 3 4 
        # 5 6 7 8
        # 7 6 5 4
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []

        while left < right and top < bottom:
            # top left -> top right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # top right -> bottom right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if left >= right or top >= bottom:
                break

            # bottom right -> bottom left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # bottom left -> top left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res