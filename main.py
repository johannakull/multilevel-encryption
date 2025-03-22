from ciphers.caesar_cipher import CaesarCipher
from ciphers.atbash_cipher import AtbashCipher
from ciphers.letter_number_cipher import LetterNumberCipher


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
        try:
            cipher_choice = int(input("\nEnter the number of the cipher you'd like to use: "))
        except ValueError:
            print("That is not a valid option. Please try again.")
            continue

        while cipher_choice not in (cipher_options.keys()):
            cipher_choice = int(input("That is not a valid option. Please try again: "))

        if cipher_choice == 1:
            cipher = CaesarCipher(text)
        elif cipher_choice == 2:
            cipher = AtbashCipher(text)
        elif cipher_choice == 3:
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
