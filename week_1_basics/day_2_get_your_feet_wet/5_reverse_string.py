# In this program we will learn about
# 1. string split
# 2. string concatenation
# 3. string length

user_input = input ( "Enter a string to reverse - ")
user_input = user_input.split ( " ")
print ( user_input[0] )

user_output = ""
str_len = len(user_input)

while ( str_len >= 1 ):
    user_output = user_output + " " + user_input[str_len - 1]
    str_len = str_len - 1
    
print ( user_output)