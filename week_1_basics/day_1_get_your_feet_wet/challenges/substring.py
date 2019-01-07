# Without using the inbuilt substring function (count), find the 
# number of occurrences of a substring in a string

s = input ( "Enter the string to be searched - ")
ss = input ( "Enter the sub-string to be searched for - ")

counter = 0

for i in range(len(s)-len(ss)) :
    for j in range(len(ss)) :
        if s[i+j] != ss[j] :
            break
    else :
        counter = counter + 1

print ( "There are ", counter, " number of occurrences of ", ss, " in ", s)


# Using inbuilt count function - Check if the answer matches
print ( "There are ", s.count(ss), " number of occurrences of ", ss, " in ", s)