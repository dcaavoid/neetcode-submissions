class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on one array, and then get the remaining elements from the other array.
        # On the left of both arrays, they come up the left portion of the merged array.
        # Given two arrays are sorted, the merged array is valid iff the largest value from one array is less or equal to the min value from the other array.
        # If not, adjust the number of elements in that array that doesn't satisfy the sorted array's rule.
        # Optimize time complexity to O(log(min(m, n))) by doing binary search on shorter array.
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A) - 1

        # Do not use "while left <= right" b/c it's possible we don't get any values from A.
        while True:
            a = (left + right) // 2     # Index of mid pointer in array A
            b = half - a - 2           # Index of the remaining elements in left portion in array B

            # Question: a little bit confused on the condition and value assignment.
            # Don't understand when it's out of bound.
            Aleft = A[a] if a >= 0 else float('-inf')   # Max val in left portion of A
            Aright = A[a + 1] if a + 1 < len(A) else float('inf')   # Min val in the right portion of A
            Bleft = B[b] if b >= 0 else float('-inf')   # Max val in the left portion of B
            Bright = B[b + 1] if b + 1 < len(B) else float('inf')   # Min val in the right portion

            if Aleft <= Bright and Bleft <= Aright:
                # If the total number of elements is odd, take the min among the two right portion.
                if total % 2:
                    return min(Aright, Bright)
                # If the total number of elements is even, take the average between min among right portions and max among left portions.
                else:  
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:    # Too many elements in A's left portion
                right = a - 1
            else:   # Too many elements in B's left portion
                left = a + 1