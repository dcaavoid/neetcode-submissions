class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Should operate in counter-clockwise and save first value into temp.
        # Given 2*2:
        # temp = [0][0]
        # [1][0] -> [0][0]
        # [1][1] -> [1][0]
        # [0][1] -> [1][1]
        # temp -> [0][1]
        # Given 3*3:
        # matrix[0][0] = temp
        # matrix[2][0] -> matrix[0][0]
        # matrix[2][2] -> matrix[2][0]
        # matrix[0][2] -> matrix[2][2]
        # temp -> matrix[0][2]
        #
        # temp = matrix[0][1]
        # matrix[1][0] -> matrix[0][1]
        # matrix[2][1] -> matrix[1][0]
        # matrix[1][2] -> matrix[2][1]
        # temp -> matrix[1][2]
        # Layer by layer, and number of layers = n // 2

        # top-left = (left, l); bottom-left = (right - offset, left)
        # bottom-right = (right, right - offset); top-right = (l, right)

        n = len(matrix)
        layers = n // 2
        for layer in range(layers):
            # Inclusive boundaries at each layer
            left, right = layer, n - layer - 1
            for l in range(left, right):
                offset = l - left   # how far along this edge
                # Save top left
                temp = matrix[left][l]

                # Move bottom left to top left
                matrix[left][l] = matrix[right - offset][left]

                # Move bottom right to bottom left
                matrix[right - offset][left] = matrix[right][right - offset]
                
                # Move top right ot bottom right
                matrix[right][right - offset] = matrix[l][right]

                # Move top left to top right
                matrix[l][right] = temp