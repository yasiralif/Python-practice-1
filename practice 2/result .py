# This is using result 
marks1= int ( input("Enter the Math number:"))
marks2= int ( input("Enter the English  number:"))
marks3= int ( input("Enter the Bangla number:"))
marks4= int ( input("Enter the Physics  number:"))
marks5= int ( input("Enter the  Chemistry number:"))

total_percentage = ( marks1 + marks2 + marks3+ marks4+marks5)/5
total_number= (marks1 + marks2 + marks3+ marks4+marks5)

if ( total_percentage>=33 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33 and marks5>=33 ):
    print( "Your are pass & and is your marks is :",total_number)

else:
    print("Your are failed in exam ", total_number)


