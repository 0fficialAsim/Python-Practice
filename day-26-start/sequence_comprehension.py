#List Comprehensions 

#Formula: new_list = [new_item for item in list]\
#Exercise 1

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

#Exercise 2 w/Strings 
name = "Adeola"
new_listTwo = [letter for letter in name]
print(new_listTwo)

"""
List Comprehsion == Sequence Comprehension 
Sequences: 
    - list
    - range
    - tuples
    - string 
Remember -> #new_list = [new_item for item in list]
"""

#Exercise 3 Range

new_listThree = [ n*2 for n in range(1,5)]
print(new_listThree)

""""
Conditional List Comprehension

Formula: new_list = [new_item for item in list if *test*]

"""

#Exercise 4 

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

#Exercise 4.5 
uppercase_names = [name.upper() for name in names if len(name) >= 5]
print(uppercase_names)

"""
Dictionary Comprehnsions 

Formula: new_dict = [new_key:new_value for item in list]
        OR
         new_dict = {new_key:new_value for (key,value) in dict.items()}

"""

#Exercise 5 
import random
studentScores = {student:random.randint(1,100) for student in names}
print(studentScores)

#Exercise 5.5
passed_students = {student:score for (student, score) in studentScores.items() if score > 60}
print(passed_students)

#FINDING MAX VALUE IN A LIST 
test = [(1, "a"), (1, "b"), (2, "c"), (2, "d")]
max(test, key=lambda x: x[0])
max(test, key=lambda x: x[0])[1] # This gets the letter value of the highest value in the list 
