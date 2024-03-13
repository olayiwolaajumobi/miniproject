list = ["apple", "banana", "cherry"]
for fr in list:
    print(fr)

courses = [70, 90, 10]
total_course = 0
for x in courses:
    total_course = total_course + x
    print(x)

print(total_course)

list = ["apple", "banana", "cherry"]
for i in range(len(list)):
    list[i] = "i eat" + list[1]

    print(list)

my_set = {2, 3, 7, 9}

my_set.add("6")

my_set.update(courses)
print(my_set)

my_set.remove(7)

print(my_set)

my_set.discard(7)
print(my_set)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "b"}

set3 = set1.union(set2)

set4 = set1.intersection(set2)

print(set3)

print(set4)


dict = {
    "brand": "ford", 
    "model" : "Mustang", 
    "year" : 1964, 
    "attribute" : {
        "height": 180,
        "eye-colour" : "brown"
    }
}  
print(dict["brand"])
print(dict["attribute"]["height"])
dict.update({"age" : 20})

print(dict)

dict.pop("model")
dict.popitem()
print(dict)
