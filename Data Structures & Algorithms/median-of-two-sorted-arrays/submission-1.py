class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Use binary search to split two arrays into merged left and right portion,
        # make sure largest value from left portion is always smaller than the smallest value from the right portion,
        # and given arrays are sorted, largest and smallest element can be retrieved through index.
        # To optimize the time complexity from O(log(m + n)), we do binary search on shorter array,
        # and the time complexity reduces to O(log(min(m, n))).
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        l, r = 0, len(A) - 1    # Left and right pointer on the shorter array for binary search.
        total = len(A) + len(B)
        half = total // 2
        
        # Because it's guaranteed to find the median.
        while True:
            i = (l + r) // 2    # Index of the last element in Aleft, and there are i + 1 elements in Aleft.
            j = half - i - 2    # Index of the last element in Bleft, and there are j + 1 elements in Bleft.

            # Set lower and upper bounds for safety.
            Aleft = A[i] if i >= 0 else float('-inf')   # If we don't take any numbers from A.
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')   # If we take all elements from A.
            Bleft = B[j] if j >= 0 else float('-inf')   # If we don't take any numbers form B.
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')   # If we take all elements from B.

            # To make a valid split,
            # the largest values in both arrays' left portions should be less than the smallest values in both arrays' right portion.
            if Aleft <= Bright and Bleft <= Aright:
                # If total nums is even, take the max of left portions and min of right portions, and then calculate mean.
                # If it's odd, take the min of the right portions.
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                # Reduce the total numbers in Aleft
                r = i - 1
            else:
                # Increase the total numbers in Aleft
                l = i + 1