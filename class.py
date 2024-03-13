# import hello
# print(hello.subt(2, 6))

# from datetime import datetime, date
# import math

# current_date = datetime.datetime.now()

# print(current_date.month)

# print(current_date.date())

# print(current_date)
# print(date(2024, 2, 29))


def must_be_greater_then_zero(value):
    if value < 0:
        raise ValueError("value less than zero")
    return value


must_be_greater_then_zero(0)

try:
    age = int(input("what is your age"))
    
except NameError:
    print("Exception")
except ZeroDivisionError:
    print("Zero exception")
finally:
    print("Error check done")

    print("HELLO WORLD")
    age()

