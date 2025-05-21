#this is class 

class person :
    def  self_info(self, name , age , id ):
        self.name = name 
        self.age = age 
        self.id = id

    def self_show(slef):
        print(f"This is my name {slef.name} and my age is {slef.age} and my id is {slef.id}")

for i in range(2):
    print(f"\n--- Person {i+1} Info ---")
    name = input("Type your name: ")
    age = input("Type your age: ")
    id = input("Type your ID: ")

p1= person()

p1.self_info(name,age,id)
p1.self_show()
# p1= person()
# name = input(str("type your name:"))
# age =input("type yor age:")
# id =input("type yor id:")

# p1.self_info(name,age,id)
# p1.self_show()
