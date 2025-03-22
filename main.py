from ciphers.caesar_cipher import CaesarCipher
from ciphers.atbash_cipher import AtbashCipher
from ciphers.madeup_cipher import MadeUpCipher


def process(original_text, method):
    processed_text = None

    while True:
        if processed_text is None:
            text_to_change = original_text
        else:
            text_to_change = processed_text

        try:
            cipher_choice = int(input("\nEnter the number of the cipher you'd like to use: "))
        except ValueError:
            print("That is not a valid option. Please try again.")
            continue

        if cipher_choice == 1:
            cipher = CaesarCipher(text_to_change)
        elif cipher_choice == 2:
            cipher = AtbashCipher(text_to_change)
        elif cipher_choice == 3:
            cipher = MadeUpCipher(text_to_change)
        else:
            print("That is not a valid option. Please try again.")
            continue

        if method == "encrypt":
            processed_text = cipher.encrypt()
        elif method == "decrypt":
            processed_text = cipher.decrypt()

        continue_encrypting = input("Would you like to apply any other ciphers? (Y/N) ").upper()
        while not (continue_encrypting == "Y" or continue_encrypting == "N"):
            continue_encrypting = input("Invalid choice. Please enter 'Y' or 'N': ")
        if continue_encrypting == "N":
            return processed_text


def main():
    original_text = input("Enter the text to be encoded/decoded: ")

    method = input("Would you like to encrypt or decrypt this text? ").lower()
    while not (method == "encrypt" or method == "decrypt"):
        method = input("Please type 'encrypt' or 'decrypt': ")

    cipher_options = {
        1: "Caesar Cipher",
        2: "Atbash Cipher",
        3: "MadeUp Cipher"
    }

    print()
    for num, cipher in cipher_options.items():
        print(f"{num}: {cipher}")

    processed_text = process(original_text, method)
    print(processed_text)


if __name__ == "__main__":
    main()
