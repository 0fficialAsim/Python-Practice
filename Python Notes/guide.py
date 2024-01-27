import keyword
import math
#from calculator import multiply

name = "Adeola" 
age = 20  
numarr = [1,2,3,4]
pi = 3.14
isAdult = True 

"""

 Python Basics 

 Data types: When defiing a variable, it is import to specify what 
 is going inside the variable 

    Find out data type by the command: 
            type(parameter)

Instead of defining a varaible by listing its data type before, 
python allows you to do it after. 
"""

print(type(name))
print(type(numarr))
print(type(pi))

#-----------------------------------------------------------------
brand: str = "Nike"
isCheap: bool = False 

def hello() -> str:
    return "hello"


"""
Common String Methods: 
Following a string variable, placing a . will show the methods for that data type. 
replace() Returns a string where a specified value is replaced with a specified value
len() Returns length of a string/other compatible data types 

Ways to concatenate 
str()
'%s'
print('{}'.format(parameter))
print(f"this {variable} is a test")
"""

print(brand.replace('N', 'L'))
print(len(brand))
print("code" in brand)

#Multiline String and Formatting String

comment = """
        This is what we 
        call a multiline 
        STRING! 
        Here is the name of the Brand {}
        age: 
        """

print(comment.format(brand))

# Reserved KeyWords 
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pas

type help("keywords") command in order to get this prompt 
"""

help("keywords")
#help("in")
print("-----------------Operators & If Statments------------------------")

"""
OPERATORS: Math, Comparison, Logic, Assignment 

Math: + , - , * , / , % , **
        -> ** refers to an exponent 
           -> ex. 2**2 means 2^2

Comparison: < , > , <= , >= , != , ==

Logical: and , or , not 
        -> Can be used in comination 

Assignment: = , += , -=, *=, **=
"""

#Power Operator 
print(2**2)


"""
If Statments 
& Ternary If Statements
"""

number = 0
if number > 0:
    print(f"number {number} is positive")
elif number == 0:
    print(f"{number}")
else:
   print(f"{number} is negative") 

#Ternary If
message = "positive" if number > 0 else " 0 or negative"
print(message)

print("-----------------Lists, Sets, & Dictionary(aka. Hashmap)------------------------\n")

"""
Lists

list = []

Methods: 
.sort
.reverse
.append --> Adds a number to the list 
.remove
.pop --> removes the last element (Good to represent a stack structre)
.clear
in / not in
del --> deletes a specfif index in your List  del numbers[0]
"""

nArr = [1 ,2 , 3, 4, -1, -20 ] #,['A', 'B']]
print(nArr[4])
#print(nArr[6][0])
print( 5  in nArr) #Is 5 in the nArr/ not in nArr
del nArr[0]
#Adding the x:y will delete numbers from list from  x to y indext 
del nArr[2:len(nArr) - 1]
print(nArr)


"""
Sets 
set = {}
*Duplicates are not allowed for a set
Sets are unordered and dont have indexes 
"""
numList = [1, 1]
numSet = {1 , 1}
LetterSet = {'A', 'A' ,'B', 'C'}
print(numList)
print(numSet)

"""
Set Operators :     
        | --> Union (Joining diff sets together)
        & --> Intersection  (Finding occurances in both sets)
        - --> Difference ( [ A - B ] Set of all elements of set A which are not in set B)
"""
lettersA  = {"A" , "B", "C", "D"}
lettersB = {"A", "E", "F"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"Union: {union} , Intersection: {intersection} , Difference: {difference}")

"""
Dictionaries 
Allows us to store Key Value pairs 
dictionary.items() returns an list of key value pairs in the dictionary 

Syntax
example = {
      key:value 
}
"""

person = {
    #Key    Value
    "Name" :"Jamal" , 
     "age" : 20, 
     "Address" : "USA"
}
print(person.items())
print(person["Name"])
print(person.get("age"))
#Update a value 
person["age"] = 100
print(person)

print("-----------------Loops------------------------\n")

"""
For Loops ! ! ! 

Looping through a set/list 
Looping through dictionary 
"""
names = ["Ade", "Temi", 
         "Mohammed", "Zaheed"]
for name in names: 
    print(name)

# for key in person: 
#     print(f" key: {key} value: {person[key]}")
#dictionary.items() returns an list of key value pairs in the dictionary 
for key , value in person.items():
    print(f" key: {key} value: {value}")

# Given a list of numbers sum up all the numbers and print it to the screen
nums = [ 1 , 3 , 5, 6 , 7, 9]

sum = 0 
for n in nums: 
    sum+=n
print(sum)



"""
While Loop 
Break & Continue 
"""

example = 0 

while example < 10: 
    example+=1 
    if example < 5:
        continue
    print(example)
else: 
    print("while loop ended")



for n in [1,2,3,4,5,6,7,8]:
    if n < 5: 
        continue 
    print(n)

"""
Range 

for number in range(a, b):
    print(number)

What this range loop provides is a way to loop through something a certain
amount of times without having to go through a data structure like a list. 

You can increase the amount of steps taken through the range by adding another paremeter
defining the step: 
    range( a, b, c)
    range( 0, 10, 2) = from 1 to 10 increase by 2 ( This would proint all even# from 1 to 10. )
"""


for number in range(1, 5):
    print(number)


print("-----------------Functions------------------------\n")

"""
Functions 
-Create functions using the *def* keyword 
Parameters and Arguments & return values
**You can set default values in the parameters until it is used in the 
parameter; 
"""
def greet(name:str , age:int = -1): 
    print(f"Hi, how are you {name} ?")
    if not age < 0: 
        print(f"Oh, your {age} years old? That's cool")
    else:
        print(f"What a cute baby")

greet("Damola",int(input("What is your age? ")))
greet("Bisola", )

def is_adult(age): 
    if age >= 16: 
        return True
    else:
        return False
    
ans  = is_adult(30)
print(ans)

print("-----------------Import Statment & Built-in Functions------\n")

"""
Built in Functions & Import Statment 
Allows us to import modules within python, your own modules or external modules
import math 

Built in java functions https://docs.python.org/3/library/functions.html
"""
print(math.pow(2, 4))

print("-----------------Creating Modules------------------------\n")
#print(calculator.divide(2, 2))
#print(calculator.add(20, 2))
#print(multiply(2, 5)) 



print("-----------------Classes & Objects------------------------\n")
class phone: 
    def __init__(self, brand, price:int):
        self.brand = brand 
        self.price = price 

    def call(self, phoneNum:str):
        print(f"{self.brand} is calling {phoneNum}")
    

Samsung = phone("Galaxy S8", 350)
iPhone= phone("iPhone 13", 1200)
print(Samsung.price)
print(iPhone.price)
iPhone.call("9083333231")

#Randomisation 

"""
Import Random Module 

Ask Python Documentation for method definitons 
"""


"""
Different ways to import 

import 

from _ import _ 

from _  import * 

import _ as t <- t is an alais name for the module
"""\


"""
Tuples in Python

Essentially the same as a list however the elements of the tuple cannot be changed/assinged new values 
Def: "Immutable"
Uses: Useful for creating a list that is meant to stay consant and does not need to change. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1      

"""



"""
Class Inheritance

A class inherinting another class and its methods.  ex.) 
    
    class Fish(Animal):
        def __init__(self):
            super().__init__()
 - Here the class fish is inheriting attributes of the Animal class.  [ Fish(Animal)]


"""
