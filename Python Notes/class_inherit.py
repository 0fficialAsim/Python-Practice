class Animal: 
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathe(self):
        print("breathin")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
         
    def swim(self):
        print("moving in water.")

#This is an example of Inheritance 