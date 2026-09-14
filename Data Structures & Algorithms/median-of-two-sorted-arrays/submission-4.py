class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search to find proper partition
        # ALeft <= BRight and BLeft <= ARight
        # A = 5 6 7
        # B = 1 2 3 4

        # Perform binary search on shorter array
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2     # Mid pointer of A
            j = half - i - 2    # Mid pointer of B

            # Special case: i and j could be out of bound
            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i+1] if i + 1 < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j+1] if j + 1 < len(B) else float("inf")

            # Find valid partition in two arrays
            if ALeft <= BRight and BLeft <= ARight:
                # Odd number
                if total % 2:
                    return min(ARight, BRight)
                # Even number
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            # Too much integers in smaller portion of A
            elif ALeft > BRight:
                right = i - 1
            # Too much integers in smaller portion of B
            else:
                left = i + 1

