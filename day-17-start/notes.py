"""
Creating my own class

- Use Class keyword followed by description. Pascal Case. 
- In order to temporaily leave a functiuon or class empty, 
  enter the "pass" keyword. 
  Attributes:

  Attributes of a class could also be added using the dot notation
  even when the class is empty. 
  ex.) user_1.id = "001" 

  Creating a Constructor/Initializing an object
         - def: to set (variables, etc) to their starting values
         at the beginnning of a program or a subprogram. 

        def __init__(self): 
            #initialise attributes 
            Attrtibues dont always need to be parameters! 
            
  Methods of Class 
        - When creating a new method, it always requires the self 
          parameter, since attrribbutes of that object may be used. 
"""

class User:
    #Creating my constructor for my class 
    def __init__(self, user_id:str,  username:str):
        self.id = user_id
        self.username = username 
        self.followers = 0
        self.following = 0 

    def follow(self, user) -> None: 
        user.followers += 1
        self.following += 1

   

user_1 = User("001", "Adeola") 
user_2 = User("001", "Micheal")
print(user_1.id + " " + user_1.username)

user_1.follow(user_2)