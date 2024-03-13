'''for i in range(1,10):

    # print(i)

    for i in range(0, 10, 2):
        print(i)
'''
# n = int(input("enter the number "))
# for i in range(1,11):
#     mul = n*i
#     print(n,"*",i,"=",mul)

# companies = ["Google", "Apple", "PWC", "Uber" ]
# for i in companies:
#     print("We will display each letter of"+i)
# for letter in i:
#     print(letter)

# while True:
#     print("Please enter your name,  ")
#     name = input()
#     if name == "Gilly":
#         break
# print("Thank you, you typed the correct name. ")
'''
x= 0
while True:
    x += 1
    if not(x % 4 or x % 7):
        break
print(x, "is divisible by both 4 and 7")
'''
# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)


'''i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is not less than 5")
    '''

'''import random
n = random.randint(1,100)
print(n)
guess = int(input("Enter an integer between 1 to 100: "))
while n != "guess":
    if guess <n:
        print("your guess is low")
        guess = int(input("Enter an integer between 1 to 100: "))
    elif guess > n:
        print("your guess is high")
        guess = int(input("Enter an integer between 1 to 100: "))
    else:
        print("you guessed it correctly!")
        break
    print()
    '''

class item:
    def __init__(self):
        print("I AM CREATED!")
        pass
    def calculate_total_price(self, x, y):
        return x * y
    
        pass
item1 = item()
item1.name = "phone"
item1.price = 100
item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
# print(item2.calculate_total_price(item2.price,item2.quantity))





