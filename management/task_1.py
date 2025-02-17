
name = input("Enter your name: ")  
age = input("Enter your age: ")  
color = input("Enter your favorite color: ") 

# Открываем файл для записи ('w' - write, перезаписывает файл)
with open("user_info.txt", "w") as file:
    file.write(f"Name: {name}\n") 
    file.write(f"Age: {age}\n")  
    file.write(f"Favorite Color: {color}\n")  

print("User information has been saved to user_info.txt")