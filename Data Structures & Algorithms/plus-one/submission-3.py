class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1

        while carry and i >= 0:
            carry = False
            if digits[i] + 1 > 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] = digits[i] + 1
            i -= 1
        
        if carry:
            digits.insert(0, 1)
        
        return digits