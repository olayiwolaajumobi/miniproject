# write a python program that accepts a sequence of comma-separated numbers from the user and generates a list and tuple of those numbers.
'''number  = input("your comma separated numbers")
'''

# write a python program that accepts user input and reverses the string.
'''name1 = input("what is your name")
name2 = name1[::-1]
print(name2)
'''
# write a python program that accepts user input and covert the string to a list of characters.
'''name = input("my name is ")
print(name.split(" "))
'''
# write a python program to get the smallest number from a list.
'''list1 = [1, 2, 5, 90, 3, 4, 1, 70,3 , 2]
print("list = ", list1)
s_num = min(list1)
print("the smallest number in the given list is", s_num)
'''

# write a python program to remove duplicates from a list.
'''list1 = (1, 2, 0, 4 ,5 ,10, 34, 10, 20)
print("original list:", list1)
list2 = []
for x in list1:
     if x not in list2:
      list2.append(x)
      print(list2)
'''



# write a python program to check if a list is empty or not

# write a python program to select an item randomly from alist
'''
import random
cities_to_visit = ["New York", "Paris", "Miami","Bogota", "Madrid", "Chicago", "Alabama", "Arizona", "Colorado", "Florida"]
print(random.choice(cities_to_visit))
'''
# QUESTION 10: write a python program to find common items in two lists.
'''
list1 = [1, 10, 10, 3, 2, 5, 100, 73, 55, 0, 1]
list2 = [20, 1, 10, 22, 55, 30, 101, 2, 1, 0, 6]


print(len(list1))
print(len(list2))

set1= set(list1)
set2 = set(list2)
if set1 and set2:
    print(set1 & set2)
else:
    print("no common numbers")
    '''
# QUESTION 11: write a  python program to convert a list of multiple integers into a single integer.
num_list = [5, 10, 34, 2, 89, 45, 3, 0, 22,1]



# QUESTION 12: write a python program to select the odd numbers from a list, and create a new list from the odd numbers.
'''odd_num = float(2, 40, 55, 100, 23, 60, 45, 22, 79, 49)
is_odd = odd_num % 2 == 1
print(is_odd)
'''
# QUESTION 13: write a python program to print the following strings in a specific format(see the output)
sam = ("Twinkle, twinkle, little star,\n How i wonder what you are!\n Up above the world so high,\n like a diamond in the sky.\n Twinkle, twinkle, little star,\n How i wonder what you are")
print(sam)
# QUESTION 14: write a python program that accepts user input and reverses the string.
'''
my_list = input("what is your list ?")
reversed_list = my_list[::-1]
print(reversed_list)
'''