class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Check for zero inputs
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize the result and the carry
        result = [0] * (len(num1) + len(num2))
        carry = 0

        # Perform the multiplication digit by digit
        for i in range(len(num1) - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                digit2 = int(num2[j])
                prod = digit1 * digit2 + carry

                # Update the result and carry
                carry = (result[i + j + 1] + prod) // 10
                result[i + j + 1] = (result[i + j + 1] + prod) % 10

            # Add the carry to the previous position
            result[i] += carry
            carry = 0

        # Convert the result to string
        result_str = ""
        for digit in result:
            result_str += str(digit)

        # Remove leading zeros
        result_str = result_str.lstrip("0")

        return result_str if result_str != "" else "0"