#input data type file  oparetion

my_file = open("myinfo.txt" ,"a")
#this is input of file 
name= input("Enetr your Name:")
roll= input("Enetr your roll :")
regs= input("Enetr your regs:")
address= input("Enetr your address:")
dep= input("Enetr your dep :")
#this is shpowing of file 
my_file.write("This is your name: "+ name)
my_file.write("\n" )
my_file.write("This is your regs:" + regs)
my_file.write("\n" )
my_file.write("This is your address:" +address)
my_file.write("\n" )
my_file.write("This is your roll:"+ roll)
my_file.write("\n" )
my_file.write("This is your dep:" + dep )
my_file.write("\n" )

my_file.close()

