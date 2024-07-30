import string

# Create the alphabet list to be used for encryption
alphabet = list((string.ascii_lowercase + string.ascii_uppercase)*2)

# Create the main function
def caesar_cipher():

    # Get the user's intention to encrypt or decrypt
    code_route = input('Enter "encrypt" to encrypt, or "decrypt" to decrypt:\n').lower()

    # Create a list of expected keywords from users
    code_route_response = ['decrypt', 'encrypt']

    # Ensure that the user only enters the required information
    while code_route not in code_route_response:
        code_route = input('Please enter the correct keyword❗, "encrypt" to encrypt, or "decrypt" to decrypt:\n')

    # Get the key to be used for encryption or decryption and catch invalid user input
    while True:
        try:
            shift_num = int(input('Please enter the key for encryption/decryption, it should be composed of only numbers:\n'))
        except:
            print('Please enter only an integer for encryption/decryption:\n')
            continue
        else:
            print('You entered a great integer\n')
            break

    # Mod the user's preferred shift number by half of the total number of characters in the alphabet in case a high shift number is used to avoid exceeding array limits
    shift_num %= 52
    shift_num += 3

    # If the user selects the decryption option, convert the shift number to a negative shift number
    if code_route == 'decrypt':
        shift_num = shift_num *-1

    # Get the text to be encrypted/decrypted from the user
    user_text = input("Please enter the text you want to encrypt/decrypt: ")

    # Create an empty string to add the encrypted/decrypted characters
    end_result = ''

    # Perform the encryption/decryption process
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            end_position = position + shift_num
            end_result += alphabet[end_position]
        else:
            end_result += char

    # Print the encrypted/decrypted message
    print(f'\nYour {code_route.capitalize()}ed message is as follows:\n{end_result}')

# Run the function
caesar_cipher()

# Ask the user if they want to run the program again or exit
rerun_response = ['yes', 'no']

# Automate the program to continue or end
rerun = True
while rerun:
    cipher_rerun = input('\nHello! Do you want to use this program again? Enter "yes" to continue or "no" to exit\n').lower()

    while cipher_rerun not in rerun_response:
        cipher_rerun = input('\nPlease enter the correct keyword❗, Enter "yes" to continue or "no" to exit\n').lower()
    if cipher_rerun == 'yes':
        caesar_cipher()
    else:
        print('Thank you for using the Caesar Cipher Program developed by Blessing. Have a nice day!\n')
        rerun = False