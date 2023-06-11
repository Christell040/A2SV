def missing_number(listz):
    temp = []
    n = len(listz)
    a = set(listz)

    for i in range(n+1):
        temp.append(i)

    b = set(temp)

    c = b - a

    return print(*c)


missing_number()
