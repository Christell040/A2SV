class Solution(object):
    def countDistinctIntegers(self, nums):
        def reverse_digits(number):
            # Convert the number to a string
            number_str = str(number)

            # Reverse the string
            reversed_str = number_str[::-1]

            # Convert the reversed string back to an integer
            reversed_number = int(reversed_str)

            return reversed_number

        rev = [reverse_digits(i) for i in nums]

        comb = nums + rev

        unique = set(comb)

        return len(unique)