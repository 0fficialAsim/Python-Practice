MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO: 1, Getting user input and looping this process after the drink is dispensed

isOperational = True
def greeting(): 
    print("Hi and welcome to my coffee shop!\n")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    

    if(choice.lower() == "off"):
       global isOperational
       isOperational = False 
    return choice


def sufficentResources(drink:str):
    currWater = resources.get("water")
    currMilk = resources.get("milk")
    currCoffe = resources.get("coffee")
  
    
    if(drink == "espresso"):
        waterNeeded =  MENU["espresso"]["ingredients"].get("water") 
        if(currWater < waterNeeded or resources.get("coffee") < 18  ):
            print("We have ran out of resouces for this an expresso.")
            return False

    elif(drink == "latte"):
        waterNeeded = MENU["latte"]["ingredients"].get("water")
        if(currWater  < waterNeeded or currMilk < MENU["latte"]["ingredients"].get("milk") or currCoffe <MENU["latte"]["ingredients"].get("coffee")):
             print("We have ran out of resouces for this latte.")
             return False
             
    elif(drink == "cappuccino"):
        waterNeeded = MENU["cappuccino"]["ingredients"].get("water")
        if(currWater  < waterNeeded or currMilk < MENU["cappuccino"]["ingredients"].get("milk") or currCoffe < MENU["cappuccino"]["ingredients"].get("coffee")):
             print("We have ran out of resouces for this latte.")
             return False
    return True
    

def processCoins( drink:str):
    finalTotal = 0 
    quarter = .25 * float(input("\nHow many quarters?"))
    dimes = .10 * float(input("\nHow many dimes? "))
    nickels = .05 * float(input("\nHow many nickels? ")) 
    pennies = .01 * float(input("\nHow many pennies? ")) 
    
    total = quarter + dimes + nickels + pennies

    if(drink == "latte"):
        finalTotal = float ( MENU["latte"].get("cost") ) 
    elif(drink == "cappuccino"):
        finalTotal = float ( MENU["cappuccino"].get("cost") ) 
    elif(drink == "cappuccino"):
        finalTotal = float ( MENU["cappuccino"].get("cost") ) 

    if(total < finalTotal): 
        print("Sorry that's not enough money. Money refuned")
        isOperational = False 
    elif(total >= finalTotal ): 
        if(total > finalTotal):
            change = total - finalTotal 
            change = round(change, 2 )
            print(f"Here is your {change} in change.")
            resources["money"] += finalTotal
            return True
    
      

def make_Coffe(drink:str, order_Ingredients ): 
    for item in order_Ingredients: 
        resources[item] -= order_Ingredients[item]
    print("Here is your latte. Enjoy! ")    

while isOperational: 
    stdIN = greeting()
    if(stdIN == "off"):
        isOperational == False 
    elif(stdIN == "report"):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[stdIN]
        if(sufficentResources(stdIN)):
            processCoins(stdIN)
            make_Coffe(stdIN ,drink["ingredients"])
    
   