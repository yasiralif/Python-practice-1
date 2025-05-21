# mowlik number ber korar cod e
n = int(input("Enter the number: "))

for i in range (2,100):
    if (n % i == 0):
        print( "thsi is not")
    break
else:
    print("thsi is prime")

