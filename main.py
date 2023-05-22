import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
SPECIAL = '!@#$%&*^|()_+'

def get_allowable_chars(uppercase, digits, special):
    characters = [LETTERS]

    if uppercase == 'y':
        characters.append(LETTERS.upper())
    if digits == 'y':
        characters.append(NUMBERS)
    if special == 'y':
        characters.append(SPECIAL)

    return characters

def select_option():
    user_choice = int(input('Your choice: '))
    if user_choice == 1:
        return print(f'Random password: {generate_password()}')
    elif user_choice == 2:
        print('Bye!')
        exit()
    else:
        print('Please select a valid option.')
        select_option()

def generate_password():
    pass_length = int(input('Please provide the password length: '))
    uppercase = input('Use uppercase letters? (y/n): ')
    digits = input('Use digits (y/n): ')
    special = input('Use special characters (y/n): ')

    random_pass = []
    characters = get_allowable_chars(uppercase, digits, special)

    for i in range(pass_length):
        random_pass.append(random.choice(random.choice(characters)))
    
    return ''.join(random_pass)

def main():
    print('''
    -- Password Generator --
    Choose option:
    1: generate password
    2: exit the program
     ''')
    select_option()

if __name__ == '__main__':
    main()