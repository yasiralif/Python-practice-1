# fucntion diye fctroial number ber koarar upay

n = int ( input("Enter the number :"))


def factroial (n):
    if ( n ==1 or n==0 ):
        return 1
    return n * factroial(n-1)

print( f"This is factroal number {factroial(n)}")