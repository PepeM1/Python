user_name = input("what is your name: ")
user_name = user_name.upper()
name = ""
for letter in user_name:
    if letter in "AEIOU":
        continue
    name+=letter
print(name)