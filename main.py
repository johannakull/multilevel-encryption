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
    text = input("Enter the text to be encrypted/decrypted: ")

    method = input("Would you like to encrypt or decrypt this text? ").lower()
    while method not in ("encrypt", "decrypt"):
        method = input("Please type 'encrypt' or 'decrypt': ")

    cipher_options = {
        "1": CaesarCipher(text),
        "2": AtbashCipher(text),
        "3": LetterNumberCipher(text),
    }

    print()
    for num, cipher in cipher_options.items():
        print(f"{num}: {cipher.__str__()}")

    while True:
        cipher_choice = input("\nEnter the number of the cipher you'd like to use: ")

        if cipher_choice not in (cipher_options.keys()):
            print("That is not a valid option. Please try again.")
            continue

        cipher = cipher_options[cipher_choice]

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
