from ciphers.caesar_cipher import CaesarCipher
from ciphers.atbash_cipher import AtbashCipher
from ciphers.letter_number_cipher import LetterNumberCipher


def main():
    print("\nWELCOME TO MULTILEVEL ENCRYPTION")
    print("Please note that any encrypted/decrypted text will be returned in uppercase.")

    text = input("\nEnter the text to be encrypted/decrypted: ")
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
        print(f"{num}: {cipher}")
    print("\nNote that the LetterNumberCipher is not suitable for text containing numbers.")

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

        print("\nWould you like to apply any other ciphers?")
        if input("Enter 'y' to continue, or press enter to skip: ").lower() != 'y':
            print(f"\nHere is your encrypted/decrypted text:\n{text}\n")
            break


if __name__ == "__main__":
    main()
