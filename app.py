# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-2])
# print(course[0:3])
# print(course[:3])
# print(course[0:])
# print(course[:])


def increment(number: int, by: int) -> tuple:
    return (number, number * by)


result = increment(5, 3)
print(result)


def save_user(**user):
    print(user)


print(save_user(id=43, name="simon", role="admin"))
