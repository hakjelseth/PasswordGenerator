import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.;:-_/?*#+&%$!"

all = uppercase_letters + lowercase_letters + digits + symbols

#Length of the password
length = 20

#amount of passwords to be generated
amount = 10

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

