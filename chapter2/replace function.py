a = '''<name> 
<roll> 
<regs>'''
print(a)

# this is replace fucntion
print(a.replace("<name>", "Alif").replace("<roll>" , "848205" ))

# this is f formet using and  replace fucntion using
print(f"This is using by replace fuction", {a.replace("<name>", "Alif").replace("<roll>" , "848205" )})
