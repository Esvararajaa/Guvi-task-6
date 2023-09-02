given_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_number = []
# Iterate each value from the list
for i in given_list:
    # Prime number should be greater than 1
    if i > 1:
        # Check the number is divisible by another number except 1 and number itself
        for j in range(2, i):
            if i % j == 0:
                break
        # Append the prime number in the empty list
        else:
            prime_number.append(i)
# Print the list of available prime number from the given list
print(f'Prime Number list: {prime_number}')