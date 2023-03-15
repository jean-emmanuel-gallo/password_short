import hashlib
import re
import json

def main():
    password_dict = {}
    process=False
    while (process == False):
        has_uppercase = False 
        has_lowercase = False 
        has_digit = False 
        has_special_char = False 

        password = input("Veuillez saisir un mot de passe :")


        if (len(password)< 8):
            print("Le mot de passe que vous avez saisi est bien trop court !")
        else : 
            if any(char in password for char in "!@#$%^&*()_-+={}[]|\:;\"'<>,.?/~"):
                has_special_char = True
        
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)

        if (has_special_char and has_uppercase and has_lowercase and has_digit):
            password_hash = hashlib.sha256(password.encode()).hexdigest() 
            print(f"Le mot de passe hâché est : {password_hash}")
            password_dict[password] = password_hash
            with open('passwords.json', 'w') as f:
                json.dump(password_dict, f)
            process = True
        elif (not has_special_char):
            print("Votre mot de passe doit cotenir au moins un caractère spécial")
        elif(not has_uppercase):
            print("Votre mot de passe doit contenir au moins une majuscule.")
        elif(not has_lowercase):
            print("Votre mot de passe doit contenir au moins une minuscule.")
        elif(not has_digit):
            print("Votre mot de passe doit contenir au moins un chiffre")

main()