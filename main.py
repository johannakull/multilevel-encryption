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

    cipher_choice = input("\nEnter the number of the cipher: ")

    caesar = CaesarCipher(original_text)


if __name__ == "__main__":
    main()
