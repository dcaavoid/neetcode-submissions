class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Use an array and store the product of each digit in reverse order.
        # Max length of a product of two numbers = len(num1) + len(num2)
        #  1 1 1    (num2)
        #  2 2 2    (num1)
        # -------
        #  2 2 2
        # res = [0 0 0 0 0 0]
        # How to remove trailing 0s in res?
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))   # Store product in reverse order

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                res[i + j] += product
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = (res[i + j] % 10)

        # Remove leading 0s after reversing
        res = res[::-1]
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        return "".join(map(str, res[i:]))