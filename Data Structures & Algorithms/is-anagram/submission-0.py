class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(list(s))
        sorted_t = sorted(list(t))
        return sorted_s == sorted_t