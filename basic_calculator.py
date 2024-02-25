#This is The Manual Calculator

print("This is the Basic Calculator")

print("Perform the calculation with manual work")

val1=input("Please Choose Your 1st Numbers from the list : 1,2,3,4,5,6,7,8,9")

val2=input("Please Choose Your 1st Numbers from the list : 1,2,3,4,5,6,7,8,9")

operator=input("Choose Your Operator Choice : +, -,*,/,**.//")


if operator=="+":
 
 print(int(val1)+int(val2))

elif operator=="-":
 
 print(int(val1)-int(val2))

elif operator=="*":
 
 print(int(val1)*int(val2))

elif operator=="/":
 
 print(int(val1)/int(val2))

elif operator=="**":
 
 print(int(val1)**int(val2))

elif operator=="//":
 
 print(int(val1)//int(val2))

else:
 
 print("Invalid Choice")



