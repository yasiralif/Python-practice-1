class Student:
    def __init__(self, name, roll):
        self.__name = name     # private variable
        self.__roll = roll

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Roll: {self.__roll}")

    def set_name(self, new_name, new_roll): 
        self.__name = new_name
        self__roll= new_roll
s1 = Student("Alif", 101)

s1.display()        

s1.set_name("Ayan",11) 
s1.display()
