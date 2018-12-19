# In this program we will enhance the number guessing game
# by including a random number rather than a hard-coded secret

import random

secret_num = random.randint(1,101)
print ( " Guess a number between 1 and 100")
num = input ()

while ( True ):
    
    if  int(num) > secret_num :
        print ( " guess a lower number " )
        num = input ()

    if int(num) < secret_num : 
        print ( " guess a higher number" )
        num = input ()
        
    if int(num) == secret_num : 
        print ( " Hurray !! you guessed it ")
        break