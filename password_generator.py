# password generator

# importing module

import random

length = int(input("Enter length of password to be generated:\n"))

available = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"

password = "".join(random.sample(available, length))

print(f"Here is your new password:\n {password}")
