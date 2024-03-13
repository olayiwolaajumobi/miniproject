# write a python program to find those numbers that are divisible by 7 and multiples of 5, between 1500 and 2700(both included).create a list of the answer
start_number = 1500
end_number = 2700
numbers = []
for number in range(start_number,end_number + 1):
    if (number % 7 == 0 and number % 5 ==0):
        print(f'The number{number} is divisible by 7 and mulitiple of 5')
        numbers.append(number)

print(start_number)
print(end_number)
# write a python program to guess a number between 1 and 9.
'''
Note: The user is prompted to enter a guess. if the user guesses wrong then the prompt appears again until the guess is correct, on a successful guess, the user will get a "well guessed!" message, and the program will exit.
'''


# write a python program to count the number of even and odd nmbers in a series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("the number of even number is:", even_count)
print("the number of odd numbers:", odd_count)
 
# QUESTION 4: Write a python function to sum all the numbers in a list
'''Sample_list = (8, 2, 3, 0, 7)
print(sum(Sample_list))
'''

# QUESTION 5: Write python function to calculate the factorial of a number(a non-negative integer). The function accepts the number as an integer

# QUESTION 6: Write a python function that accepts a string and counts the number of upper and lower case letters.
str1 = 'The quick Brow Fox'
lower = 0
upper = 0
for character in str1:
    if character.islower():
        lower=lower+1
    elif character.isupper():
        upper=upper+1
        print("lower count:", lower)
        print("upper count", upper)

