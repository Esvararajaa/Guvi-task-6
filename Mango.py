bag_count = int(input('Enter the number of bags required: '))
N = []
for o in range(1, bag_count+1):
    ele = int(input(f'Mangoes in {o} bag: '))
    N.append(ele)
print()
print(f'List of mangoes in each bags: {N}')
# Total Number of mangoes
Total = sum(N)
print()
# Total Number of students in guvi
M = int(input('Enter the total number of Students in GUVI: '))
# On an average share to each student
n = Total // M
# Remaining number of Mangoes
r = Total % M
Result = []
for i in range(M):
    Result.append(n)
    i += 1
for j in range(r):
    Result[j] = Result[j] + 1
print()
print(f'Share to each student is {Result}')