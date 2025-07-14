def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("-------")
    return wrapper
def my_old():
    print("this is new")

a = my_decorator(my_old)
a()
  