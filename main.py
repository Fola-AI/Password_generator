import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Option 1
#To Generate a password that follows sequentially in letters,symbols and numbers

password = " "
for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)

print(password)

#Option 2
#Code below scrambles the password rather than prints sequentially just as the one above
password_list = []

for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)

print (password_list)   #Prints it as a list and sequentially
random.shuffle(password_list)       #Shuffle function shuffles and scrambles the password
print(password_list)


