items = [
    ("product1", 10),
    ("product1", 9),
    ("product1", 12)
]

# prices = []

# for item in items:
#     prices.append(item)
#     print(item[1])

prices = list(map(lambda item: item[1], items))
print(prices)
