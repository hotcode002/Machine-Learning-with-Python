print ( "Prime number program ")
user_input = input ( " Enter a number greater than 1 - ")
user_input = int(user_input)

found_prime_flag = True

for i in range ( 2, user_input):
    if user_input % i == 0:
        print ( user_input, " is not a prime number")
        print ( "it is divisible by", i)
        found_prime_flag = False
        break
else:
    print ( user_input, "is a prime number")