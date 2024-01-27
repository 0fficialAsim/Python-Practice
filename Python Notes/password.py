import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Letters
password =  ""
prePass = []
for lett in range(0, nr_letters ): 
  """
  random = random.randint(0, len(letters) - 1)
  password = password + letters[random]
  """
  #Use random.choice() to get a random element from sequence.
  #Or use the naive method I created. 
  rand_lett = random.choice(letters)
  prePass.append(rand_lett)

for num in range( 0 , nr_numbers ) :
   rand_num = random.choice(numbers)
   prePass.append(rand_num)
  
for symbol in range(0 ,nr_symbols ):
  rand_sym = random.choice(symbols)
  prePass.append(rand_sym)

length = len(prePass)
for char in range( 0 , length ):
  instance = random.choice(prePass) 
  password += str(instance)
  prePass.remove(instance)

print(password)