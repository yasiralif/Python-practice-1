class MyClass:
    def __init__(self):
        self.__private_var = 10  # Private member

obj = MyClass()
print(obj.__private_var)  # ❌ Error: AttributeError
