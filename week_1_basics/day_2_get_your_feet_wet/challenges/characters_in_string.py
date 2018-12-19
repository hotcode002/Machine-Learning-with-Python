# In this challenge, we find out how many times a character occurs in a string

s = input ( "Enter the string to be searched - ").upper()
a = input ( "Enter the alphabet to be searched - ").upper()

counter = 0

for i in range(len(s)) :
    if a == s[i] :
        counter = counter + 1

print ("The character ",a," occurs ", counter, " number of times")

# Using the count() function - This becomes just a one liner.
# print ("The character ",a," occurs ", s.count(a), " number of times")