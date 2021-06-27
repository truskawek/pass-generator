import sys
import random
import string

password = []
characters_left = int



def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters > characters_left or number_of_characters < 0:
        print('This number is out of range <1,{password_len}>'.format(password_len=password_len))
        sys.exit(0)
    else:
        characters_left -= number_of_characters

def get_correct_answer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number")
                continue
            else:
                break
        except ValueError:
            print("Enter correct value")
        
    return value

def summarize():
    print('Password length: {password_len}'.format(password_len = password_len))
    print('Lowercase letters: {lowercase_letters}'.format(lowercase_letters = lowercase_letters))
    print('Uppercase letters: {uppercase_letters}'.format(uppercase_letters = uppercase_letters))
    print('Special characters: {special_chars}'.format(special_chars = special_chars))
    print('Digits: {digits}'.format(digits = digits))


password_len = get_correct_answer("how long your password needs to be? \n")

if password_len < 5:
    print("Your password is waaaaay to short. Please enter more than 5 characters")
    sys.exit(0)
else:
    characters_left = password_len

lowercase_letters = get_correct_answer("How many lowercase letters you want to have? \n")
update_characters_left(lowercase_letters)

uppercase_letters = get_correct_answer("How many uppercase letters you want to have? \n")
update_characters_left(uppercase_letters)

special_chars = get_correct_answer("How many special characters you want to have? \n")
update_characters_left(special_chars)

digits = get_correct_answer("How many digits you want to have? \n")
update_characters_left(digits)

if characters_left > 0:
    print("You did not use all of available characters. Your password will be populated with lowercase letters")
    lowercase_letters += characters_left

summarize()

for _ in range(password_len):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_chars > 0:
        password.append(random.choice(string.punctuation))
        special_chars -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)

print("Your password is: ", "".join(password))


