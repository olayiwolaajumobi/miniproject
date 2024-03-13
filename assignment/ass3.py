# # create a BMI calculator, has the user to input their height, then ask for their weight then print out the BMI, use format string to present your answer
# the_height = int(input("enter the height in cm: "))
# the_weight = float(input("enter the weight in kg: "))

# BMI = the_weight / (the_height/100)**2
# print(BMI)

# if BMI >= 100:
#     print("Normal")





# # write a python program that calculates the area of a circle based on the radius entered by the user

# # Area = PI * R ** 2

# # hint use math.pi for the value of PI


# PI = 3.14
# r = float(input("enter radius "))

# area = PI * r ** 2
# a = 3.14159 * r * r
# print("area of circle =" , a)


# write a python program that determines whether a given number(accepted from the user) is even or odd, and print an appropriate message to the user

num = float(input("enter number: "))

is_even = num % 2 == 0

is_odd = num % 2 == 1


print(is_even)
print(is_odd)


'''input("number")
if number >= 300:
    print ("even")
if number <=250:
    print ("odd")
'''


# write a python program that determines wheather  a given number(accepted from the user) is a prime number, and print an appropriate message to the user

the_number = input("Enter your number ")
prime_number = input()

# write examples code with all the comparison, logical, identity and membership operators

# Comparison 


# Logical
a = 10
b = 22
 

# Identity

x = 2
y = 6


# Membership  
alpha = ("alphabelts")
comp = ("components")

print("hab" in alpha)
print("ZE" in comp)
