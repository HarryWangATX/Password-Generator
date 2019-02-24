import random


char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password = ""

while True:
  user_input = input("How long would you like your password to be? ")

  try:
     val = int(user_input)
  except ValueError:
    print("Please enter a number")
    break

  user_input = int(user_input)

  for i in range(user_input):
    password += random.choice(char)
  print("")
  print(str(password))
  
  print("")
  x = input("Would you like to make another password? ")
  
  try:
    val = str(x)
  except ValueError:
    print("Please enter yes or no.")
    break
  
  if x == "yes" or x == "Yes":
    a = 0
  else:
    break
