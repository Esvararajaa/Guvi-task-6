list1 = [4, 2, -3, 1, 6]
num = len(list1)


def add_sublist_zero(l, n):
    # iterate element from the list
    for i in range(n):
        add = l[i]
        # compare to the total sum
        if add == 0:
            return True
        # add the iterated element with the next iterated element
        for j in range(i + 1, n):
            add = add + l[j]
            # compare to the total sum
            if add == 0:
                return True
    return False


if add_sublist_zero(list1, num):
    print('sub list is available')
else:
    print('sub list is not available')
