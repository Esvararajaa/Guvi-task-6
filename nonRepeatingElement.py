k = [40, 20, 30, 20, 20, 30, 10, 50, -20, 60, 60, -20, -20, 40]
m, n, result = [], [], []
for i in k:
    # list with numbers without repeated elements
    if i not in m:
        m.append(i)
    # list with only repeated elements
    else:
        n.append(i)
# compare the m & n to find non-repeating elements, append in result
for j in m:
    if j not in n:
        result.append(j)
print(f'Given list = {k}')
# print the first non-repeating elements in the result list
print(f'Result = {result[0]}')