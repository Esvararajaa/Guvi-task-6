lis = [10, 501, 22, 37, 100, 999, 87, 351]
# used to take count
m = 0
# iterate the list
for n in lis:
    while n != 1:
        j = 0
        # to sum the square of each digit in the iterated number
        for i in str(n):
            i = int(i)
            j = j + i**2
        # if the sum is equal to one at any point of time in the loop, number is happy
        if j == 1:
            # print('happy')
            m += 1
            break
        # if the sum is equal to four at any point of time in the loop, number is unhappy
        elif j == 4:
            # print('unhappy')
            break
        else:
            n = j
            continue
    else:
        m += 1
        # print('happy')
print(f'Total count of happy numbers in the list: {m}')