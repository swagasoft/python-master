
try:
    age = int(input("age: "))
except ValueError as ex:
    print('You did not enter a valid age')
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print()
else:
    print('No exception was thrown')
