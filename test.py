l = []
print ( " enter your numbers. type 'exit' to exit -  ")

while ( True ) :
    input_str = input()
    if input_str.upper() == "EXIT" :
        break
    l.append(int(input_str))


print ( "The list you entered is", l )

# sort the list
l.sort()
print ( "Here is the sorted list", l )