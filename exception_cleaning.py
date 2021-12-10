# try:
#     file = open('exercise')
#     age = int(input("age: "))
# except(ValueError, TypeError, ZeroDivisionError):
#     print('You did not enter a valid age')
# else:
#     print('No exception')
# finally:
#     # the finally block will always run
#     file.close()

try:
    with open('exercise') as file:
        print('file open')
    age = int(input("age: "))
except(ValueError, TypeError, ZeroDivisionError):
    print('You did not enter a valid age')
else:
    print('No exception')
finally:
    file.close()
