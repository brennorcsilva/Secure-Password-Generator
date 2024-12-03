from random import choice
import string


special = [ '!', '@', '#', '$', '%', '&', '*', '_', '<', '>' ]
special_Char = ''.join(special)

def get_preferences():
    password_size = int(input('Input how many characters do u want in your password:'))
    if password_size <= 0:
        print('Invalid password size! \nTry again! Remember to set a minimum password length!')
        return None
    
    include_uppercase = input('Do you want uppercase? (y/n): ').lower() == 'y'
    include_numbers = input('Do you want numbers? (y/n): ').lower() == 'y'
    include_special = input('Do you want special characters? (y/n): ').lower() == 'y'

    return password_size, include_uppercase, include_numbers, include_special

def character_pool(include_uppercase, include_numbers, include_special):
    chars = string.ascii_lowercase

    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += special_Char
    
    return chars
    
def generate_password(password_size, chars):
    return ''.join(choice(chars) for _ in range(password_size))

def main():
    preferences = get_preferences()
    if not preferences:
        return
    
    password_size, include_uppercase, include_numbers, include_special = preferences

    chars = character_pool(include_uppercase, include_numbers, include_special)

    if not chars:
        print('No character types selected! Unable to generate a password!')
        return
    secure_password = generate_password(password_size, chars)

    print('Generated password:', secure_password)

if __name__ == '__main__':
    main()