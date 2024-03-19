import random

# characters=[]
# for i in range(33,127):
#     characters.append(chr(i))

# # print(characters)

# def generatePassword(length):
#     password=[]
#     for i in range(length):
#         password.append(random.choice(characters))
#     return "".join(password)
# print(generatePassword(16))

class PasswordGenerator:
    def __init__(self):
        self.characters=[chr(i) for i in range(33,127)]
    def generatePassword(self,length):
        password=[]
        for i in range(length):
            password.append(random.choice(self.characters))
        return "".join(password)

pwd=PasswordGenerator()
try: 
    user_input=int(input("Enter the Length Password:"))
    passcode=pwd.generatePassword(user_input)
    print(passcode)
except Exception as e:
    print(e)