"""
    PASSWORD GENERATOR By Samuel Lunghe
"""
import random
class PasswordGenerator:
    def __init__(self):
        self.characters=[chr(i) for i in range(33,127)]
    def generatePassword(self,length):
        password=[]
        for i in range(length):
            password.append(random.choice(self.characters))
        return "".join(password)



def main(): 
    pwd=PasswordGenerator()
    try: 
        user_input=int(input("Enter the Length Password:"))
        passcode=pwd.generatePassword(user_input)
        print("-"*80)
        print("Password Generated:",passcode)
        print("-"*80)
    except Exception:
        print("Invalid Input...")
        main()
        # print(e)
print("-"*80)
print("="*30+"PASSWORD GENERATOR"+"="*30)
print("-"*80)
main()