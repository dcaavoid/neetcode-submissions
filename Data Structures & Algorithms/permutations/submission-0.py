class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 2. Iteration
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        
        return perms

        # 1. Recursion: build permuations without first element first,
        #    and then try to insert the first element to every position in each permuation.
        # Let N be the length of nums.
        # Time: O(N! * N) since there are (N-1)! permuations, and in each permuation there are N positions to insert, which inserting takes O(N^2) times.
        #       (N-1)! * N^2 = N!*N
        # Space: output takes O(N!*N) as there are N! number of permutations, and each permutation takes N space.
        #        In recursion: 1. nums[1:] takes O(N^2) space
        # Base case:
        # if len(nums) == 0:
        #     return [[]]
        
        # # Recursive
        # perms = self.permute(nums[1:])
        # res = []

        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        
        # return res