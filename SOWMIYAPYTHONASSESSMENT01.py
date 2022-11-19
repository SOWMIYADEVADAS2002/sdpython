#assignment 01

def login():
  username = input ("Enter the username ")
  password = input ("Enter the password ")
  confirm_password = input ("Enter the confirm password ")
  if(password == confirm_password ):
    print("Login Successful")
  else:
    print("Login Failed")
login()


#assignment02

num = int(input ("Enter the num "))
if (num % 2) == 0:
    print("The number is even ")
else:
    print("The number is odd")


#assignment03
    fruits=["plum","cherry","blueberry","gooseberry","strawberry",]
FRUIT = [x for x in fruits if "e" in x]
BERRY = [x for x in fruits  if "r" in x]
FRESH = [x for x in fruits  if "s" in x]
HEALTHY = [x for x in fruits  if "y" in x]
print(FRUIT)
print(BERRY)
print(FRESH)
print(HEALTHY)


