n = [4, 4, 5, 6, 7, 8, 9, 0, 0]
m = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
k = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


def duplicate(inp):
    p = []
    d = []
    for i in inp:
        # list with non-repeating elements list
        if i not in p:
            p.append(i)
        # list with repeated elements list
        elif i not in d:
            d.append(i)
    # return the repeated elements list
    return d


print(duplicate(n))
print(duplicate(m))
print(duplicate(k))