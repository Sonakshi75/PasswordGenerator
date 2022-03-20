print("Welcome to the pyPassword Generator")
import random
lettersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbolsList = ['!','@','#','$','%','^','&','*','(',')']
numbersList = [1,2,3,4,5,6,7,8,9,0]
letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))
password = []
for i in range(0,letters):
    password.append(random.choice(lettersList))
for i in range(0,symbols):
    password.append(random.choice(symbolsList))
for i in range(0,numbers):
    password.append(random.choice(numbersList))
print(password)
random.shuffle(password)
password_string=""
for i in password:
    password_string+=str(i)
print(password_string)
