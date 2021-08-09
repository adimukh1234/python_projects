# email slicer

email = input("Enter your email: ").strip()
user = email[: email.index("@")]
domain = email[email.index("@") + 1:]

message = f"Your username is {user} and your domain is {domain}"
print(message)
