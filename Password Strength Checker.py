# #q3: Password Strength Checker
password = input("Enter a password: ")

uppercase = 0
lowercase = 0
digits = 0
special_chars = 0

for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1

print("\nTotal uppercase letters:",uppercase)
print("Total lowercase letters:",lowercase)
print("Total digits:",digits)
print("Total special characters:",special_chars)