#this is decorator function



def decator(fucn):
    def date():
        print("this is 1st line")
        fucn()
        print("this is 2nd line")
        fucn()
    return date  # ✅ ঠিক এটা return করা লাগবে

@decator
def say_hello():
    print("Hello!")

say_hello()
