# factorial number ber koar code 
n = int ( input("Enter the number : "))

factorial= 1
for i in range (1, n+1):
    factorial = factorial*i
    
print(f"This is numer of your enter {n} and this is factorial numer {factorial}")