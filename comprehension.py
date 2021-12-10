values = []
for x in range(5):
    values.append(x * 2)
print(values)


value2 = [x * 2 for x in range(5)]
print(value2)

value3 = {x: x * 2 for x in range(5)}
print(value3)
