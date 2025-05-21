# Get user input
data = input("Enter text to write to file: ")

# Open the file in write mode
with open("output.txt", "w") as file:
    file.write(data + "\n")
    
print("File written successfully.")
