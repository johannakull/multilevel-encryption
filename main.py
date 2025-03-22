from ciphers.caesar_cipher import CaesarCipher
from ciphers.atbash_cipher import AtbashCipher
from ciphers.letter_number_cipher import LetterNumberCipher


def get_int(user_input):
    try:
        integer = int(user_input)
    except ValueError:
        user_input = input("That is not a valid option. Please try again: ")
        return get_int(user_input)
    else:
        return integer


def main():
    text = input("Enter the text to be encoded/decoded: ")

    method = input("Would you like to encrypt or decrypt this text? ").lower()
    while method not in ("encrypt", "decrypt"):
        method = input("Please type 'encrypt' or 'decrypt': ")

    cipher_options = {
        1: "Caesar Cipher",
        2: "Atbash Cipher",
        3: "LetterNumber Cipher"
    }

    print()
    for num, cipher in cipher_options.items():
        print(f"{num}: {cipher}")

    while True:

        cipher_choice = input("\nEnter the number of the cipher you'd like to use: ")
        cipher_choice_int = get_int(cipher_choice)

        while cipher_choice_int not in (cipher_options.keys()):
            print("That is not a valid option. Please try again.")
            continue

        if cipher_choice_int == 1:
            cipher = CaesarCipher(text)
        elif cipher_choice_int == 2:
            cipher = AtbashCipher(text)
        elif cipher_choice_int == 3:
            cipher = LetterNumberCipher(text)

        if method == "encrypt":
            text = cipher.encrypt()
        elif method == "decrypt":
            text = cipher.decrypt()

        continue_processing = input("\nWould you like to apply any other ciphers? (Y/N) ").upper()
        while continue_processing not in ("Y", "N"):
            continue_processing = input("Invalid choice. Please enter 'Y' or 'N': ").upper()
        if continue_processing == "N":
            print(text)
            break


if __name__ == "__main__":
    main()
