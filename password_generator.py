import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.;:-_/?*#+&%$!"

all = uppercase_letters + lowercase_letters + digits + symbols

#Length of the password
length = 20

password = "".join(random.sample(all, length))

print(password)

