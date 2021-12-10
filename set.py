

numbers = [1, 1, 2, 3, 4]
# unique = set(numbers)
# print(unique)

first = set(numbers)
second = {1, 5}


# print union in set
print(first | second)

# intersection of a set (numbers that exist in  both set)
print(first & second)

#  difference between two set
print(first - second)

# symatric difference
print(first ^ second)

if 1 in first:
    print("yes")
