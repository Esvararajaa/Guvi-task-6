def find_triplet(array, length, total):
    # Checking the from 0 index till end
    for i in range(0, length):
        # Checking the from next of i index till end
        for j in range(i + 1, length):
            # Checking the from next of j index till end
            for k in range(j + 1, length):
                # Checking the addition of iterated value to the given total
                if array[i] + array[j] + array[k] == total:
                    return array[i], array[j], array[k]


# Given list
arr = [10, 20, 30, 9]
print()
# Print the given list
print(f'Original list: {arr}')
print()
# Finding the length of the list
n = len(arr)
# calling the function and saving in the valiable
lst = find_triplet(arr, n, 59)
# Printing the output
print(f'Triplet to the sum of 59: {lst}')
