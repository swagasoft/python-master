point = {"x": 1, "y": 2}

# list()
# set()
# tuple()
#  you can also use the dictionary
point2 = dict(x=1, y=2)

point["k"] = 5
point["m"] = 5

print(point)
if "a" in point:
    print(point["a"])

print(point.get("b"))

# if no element return 0 by default
print(point.get("b", 0))

#  to delete an item
del point["x"]

# looping dictionaries
for key in point:
    print(key, point[key])


# looping dictionaries
for x in point.items():
    print(x)


# looping dictionaries
for key, value in point.items():
    print(key, value)
