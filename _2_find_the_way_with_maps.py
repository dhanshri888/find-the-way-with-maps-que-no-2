# Find the way with Maps

# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


lst = [1, 2, 3, 4, 5, 6, 7]

print("sample list:",lst)

result = list(map(lambda x: x+ x+ x ,lst))

print("Triple of list numbers: ")

print(result)