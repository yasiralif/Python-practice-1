# This is using by factorial number
n = int ( input("enter the nuber: "))
def fact ( n):
    if n==1:
        return False
    elif (n==2):
        return True
    else :
        for i in range (2,n):
            if (n % i==0):
                return True
            
result =fact(n)

print(f"This is {n} input number and this is {result}")