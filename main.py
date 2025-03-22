from ciphers.caesar_cipher import CaesarCipher
from ciphers.atbash_cipher import AtbashCipher


def main():
    original_text = input("Enter the text to be encoded/decoded: ")

    print("\nWhich of the following ciphers would you like to use?\n")

    cipher_options = {
        "1": "Caesar Cipher",
        "2": "Atbash Cipher",
    }

    for num, cipher in cipher_options.items():
        print(f"{num}: {cipher}")

    while True:
        cipher_choice = input("\nEnter the number of the cipher: ")

        continue_encrypting = input("Would you like to apply any other ciphers? (Y/N) ").upper()
        if continue_encrypting == "Y":
            print("\nWhich of the ciphers would you like to use?")
        else:
            break


if __name__ == "__main__":
    main()
