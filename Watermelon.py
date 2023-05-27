import random
import math


def divide_watermelon(w):
    # Check if the weight is even and greater than 2
    if w % 2 != 0 or w == 2:
        return False  # Cannot divide the watermelon as desired

    return True # Can divide the watermelon as desired


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def even_splitter(num):
    if divide_watermelon(num):
        indicator = True
        while indicator:
            a = random.randrange(2, num)  # generate random number within the bounds
            b = random.randrange(2, num)  # generate random number within the bounds
            if is_even(a) and is_even(b) and (a + b) == num:
                indicator = False
                print(f"Yes {a} + {b}")
                break
            else:
                continue

    else:
        print("Even division isn't possible")


numb = int(input("Enter the weight__"))
print(even_splitter(numb))
