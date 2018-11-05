secret_num = 59
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