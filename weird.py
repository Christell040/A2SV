def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False


number = int(input("Enter number__"))

if is_odd(number):
    print("Weird")
if is_even(number) and (1 < number < 5):
    print("Not Weird")
if is_even(number) and (6 <= number <= 20):
    print("Weird")
if is_even(number) and number >= 20:
    print("Not Weird")
