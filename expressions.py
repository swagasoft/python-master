items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]

# prices = []
# for item in items:
#     if item[1] >= 10:
#         prices.append(item[1])
# print(prices)


# filtered = list(filter(lambda item: item[1] >= 10, items))

# print(filtered)

filtered = [item for item in items if item[1] >= 10]
print(filtered)
