#names = ["Alice", "Bob", "Charlie", "Diana"]
#for name in names:
   #print(name)


count = 0
while count < 5:
  #  print("Count:", count)
   # print("hello")
    count += 1  

    actual_password = "admin123"
attempts = 3
while attempts > 0:
    entered_password = input("Enter the password: ")
    if entered_password == actual_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
