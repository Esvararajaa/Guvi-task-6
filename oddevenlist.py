given_list = [10, 501, 22, 37, 100, 999, 87, 351]
odd_list = []
even_list = []

# Find the even and odd numbers and append to the respective above list
for i in given_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
# Print the output list
print(f'Given list: {given_list}')
print(f"Even numbers in the given list: {even_list}")
print(f"Odd numbers in the given list: {odd_list}")