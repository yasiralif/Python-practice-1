# 3 number o f largest number 
number_1= int(input("Enter the 1 number: "))
number_2= int(input("Enter the 2 number: "))
number_3= int(input("Enter the 3 number: "))

def largest ():
    if (number_1>number_2 and number_1>number_3):
        print("The largest number of :",number_1)
    elif(number_2>number_1 and number_2>number_3):
        print(" The largest number is : " , number_2)
    else:
        print("The largest number is : ", number_3)
largest()