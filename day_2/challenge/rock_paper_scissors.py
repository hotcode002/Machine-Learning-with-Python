import random
options = ['r','p','s']

# Rock > Scissors > Paper > Rock

print ( "press 'e' to exit")
while ( True ) : 
    computer_choice = options[random.randint(0,2)]
    user_choice = input ( ' (r)ock, (p)aper or (s)cissors - ' )
    
    if user_choice == "r" or user_choice == "p" or user_choice == "s" :
        print ( "computer choice ",computer_choice)
        print ("you entered ", user_choice)
        if user_choice == computer_choice :
            print ( "tie - try again")
            continue
        elif user_choice == "r" :
            if computer_choice == "s" :
                print ( "you win. play again !!")
            else : 
                print ( "you loose. play again !!")
        elif user_choice == "p":
            if computer_choice == "r" :
                print ( "you win. play again !!")
            else : 
                print ( "you loose. play again !!")            
        elif user_choice == "s":
            if computer_choice == "p" :
                print ( "you win. play again !!")
            else : 
                print ( "you loose. play again !!")   
    elif user_choice == "e" :
        print ( "exiting game")
        break
    else :
        print ( "enter either 'r' or 'p' or 's' ")
        continue
    