# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)


# usng lamda expression
items.sort(key=lambda item: item[1])
print(items)
