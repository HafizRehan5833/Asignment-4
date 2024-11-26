#. Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters

import random
import string

def generate_random_password(pass_length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    special_character=string.punctuation

    all_charcters=lowercase+uppercase+digits+special_character

    if pass_length < 4:
        raise ValueError ("Atlest more than 4 character required to generate a random password..")

    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_character)
    ]    

    password += random.choices(all_charcters, k=pass_length - 4)

    random.shuffle(password)

    return ''.join(password)



user_input_length=int(input("Enter Length of a password: "))

func=generate_random_password(user_input_length)
print("Your password with using some AI functions are given:\n\t\t\t\t\t\t\t",func)

