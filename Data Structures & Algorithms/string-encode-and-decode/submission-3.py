class Solution:
    # Intuition: shift each letter in by two units in encoding, and then shift back in decoding
    # Use number#-combination: number=length of each word, #=start of word

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += ("#")

            for c in s:
                res += c
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            # Update j every time with a new index i
            j = i

            # Find the length of each number
            # Considered the case where the length is more than one digit
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])    # Convert into integer
            word = s[j+1: j+length+1]
            res.append(word)
            i = j + length + 1   # Update based on pointer j
        
        return res
