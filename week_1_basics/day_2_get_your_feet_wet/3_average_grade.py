# Calculate mean without using list data structure
# In this program, we will learn about 
# 1. int vs float

print ( "Enter grades to calculate mean/average grade. type e to exit")
sum     = 0
mean    = 0
count   = 0
while True :
    grade = input ( " - ")
    if grade == "e" :
        break
    else :
        grade   = float(grade)
        sum     = sum + grade
        count   = count + 1

mean = sum/count

print ( "Average class grade is ",mean)

