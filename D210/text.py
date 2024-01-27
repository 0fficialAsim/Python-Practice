import math


def primes(n):
    """Returns all prime numbers from 2 to n (excluding n) """
# YOUR CODE HERE
    isPrime = True
    ansList = [] 

    if( n == 2):
        ansList.append(n)
    
    for num in range(2, n):
        isPrime = True 
        for j in range( 2 , num):
            if( num % j == 0):
                isPrime = False;  
        if(isPrime == True):
            print(num)
            ansList.append(num)
            
    return ansList

def factor(n):
    """Return all the prime factors of n."""
    # YOUR CODE HERE
    list = primes(n)
    
    conditionMet = False
    prime_Factors = []
    i = 0
    while(conditionMet != True):
        if( n % list[i] == 0):
            prime_Factors.append(list[i])
            
            n =  n / list[i]
            
            if( n == 1):
                conditionMet = True; 
            
        elif(n % list[i] != 0):
            i += 1
    
    return prime_Factors

def increasing_digits(n):
    """ Returns the number of integers from 1 to $n$ (inclusive) 
    that have all digits in increasing order, where $n$ is
    given as a parameter. 
    """
    digitCount = 0
    countToN= 1
    
    while(countToN <= n):
        
        if(countToN >=10):
            digits = str(countToN)
            prevDigit = int ( digits[0:1] ) 
            increase = True
            for i in digits[1:]:
                if(int(i) <= prevDigit):
                    increase = False 
                    break 
            if(increase): 
                digitCount+=1
                
        elif(countToN < 10):
            digitCount+=1
        
        countToN+=1
    return digitCount
    
        
def stats(ints):
    """ 
    Returns the mean, median, and standard deviation (in that order) of a 
    list of integers given as a parameter. 
    """
    #Mean
    
    ansList= [] 
    sum = 0
    for i in ints:
        sum += i

    mean = sum / len(ints) 
    ansList.append(mean)
    
    #Median 
        #median 
    if(len(ints) % 2 != 0):
        ansList.append(ints[int(len(ints) / 2)])
    else:
        i = int(len(ints) / 2)
        median = ( ints[i] + ints[i-1] ) / 2  
        ansList.append(median)
        
    #standard deviation 
    partone =  1 / (len(ints) - 1)  
    summation = 0  
    summation += math.pow(( i - mean) , 2)
        
    stanD = math.sqrt( partone * summation ) 
    ansList.append(stanD)     

    return ansList



def threeSum(nums):
    found = False

    n = len(nums)
    ans = [] 

    for i in range(0, n-2):
 
        for j in range(i+1, n-1):
 
            for k in range(j+1, n):
 
                if (nums[i] + nums[j] + nums[k] == 0):

                    tupleAns = (nums[i], nums[j], nums[k])
                    ans.append(tupleAns)

                    print(nums[i], nums[j], nums[k])
                    found = True
 
    # If no triplet with 0 sum
    # found in array
    if (found == False):
        return ans
 


def reverse_sorted_words(filename):
    names = []
    isCapital =  []
    with open(filename, "r") as file:
        #count = 0
        for line in file:
            for name in line.split():
                #count += 1
                if(name.istitle()): 
                    isCapital.append(name) 
                names.append(name.lower())
    names.sort(reverse=True)

    for capital in isCapital:

        for i, name in enumerate(names) :
            if(names[i] == capital.lower()):
                print(capital)
                names[i] = capital
                print(names[i])
                break
    
    return names


print(reverse_sorted_words("words.txt"))