#file oparetion on write mood
my_file = open("wi=rite mood.txt" ,"w")
name= input("type your name:")
my_file.write("this is  write mood file" +name)
my_file.close()
