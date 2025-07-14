import math
# lenght = ( "enter the lenght :")
# width = ( " Enter the widht :")

# def area ():
#     lenght = int (input ( "enter the lenght :"))
#     width =int (input ( " Enter the widht :"))
#     rectan = lenght * width
#     print("Area of :", rectan)
# area()


def is_prime(n):
    if (n  == 0):
        return False  # 1 বা এর নিচের সংখ্যা প্রাইম নয়
     # 2 থেকে √n পর্যন্ত চেক
    elif (n % 2 == 1):
        return False
    else:
        return True  # কোনো সংখ্যা দিয়ে ভাগ গেলে প্রাইম নয়
    
n= 45 
print(is_prime(n))



