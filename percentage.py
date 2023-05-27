def percentage_find(phrase,character):
    x = len(phrase)
    y = phrase.count(f"{character}")

    percentage = (y / x) * 100

    return percentage.__round__()



a = input("Enter the phrase__")
b = input("Enter the character__")

print(percentage_find(a,b))