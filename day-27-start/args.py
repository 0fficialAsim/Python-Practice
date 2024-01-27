

# Functions with DEFAULT vaues
def sum(x=2, y=5):
    return x+y

#Functions with Unlimited Arguments *args
def add(*args):  #Args = Arguments 
    sum = 0
    for n in args: 
        sum+=n
    return sum

print(add(2,4,5,6,7,8))

#Functions w/ *kwargs, Keyworded Arguements 

def calculate(n,**kwargs): # Unlimited Keyword arguements, *keyword
    print(kwargs)
    
    if 'add' in kwargs.keys():
        n += add(kwargs['add'])
    n*= kwargs['multiply']
    print(n)


calculate(2,add=3, multiply = 4 )



#Using Keyword Arguments when making a class 

class Car: 
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')

car = Car(make = 'Nissan', model = 'Pathfinder ')