from ciphers.cipher import Cipher
from constants import LETTER_TO_INDEX_MAP, INDEX_TO_LETTER_MAP


class LetterNumberCipher(Cipher):

    def __init__(self, original_text):
        super().__init__(original_text)

    name = "LetterNumber Cipher"

    def encrypt(self):
        encrypted_text = []
        for char in self.original_text:
            if char in LETTER_TO_INDEX_MAP:
                new_char = LETTER_TO_INDEX_MAP[char] + 1
                encrypted_text.append(f"{new_char} ")
            elif char == " ":
                encrypted_text.append("0 ")
            else:
                encrypted_text.append(f"{char} ")
        return "".join(encrypted_text)

    def decrypt(self):  # doesn't work if there are numbers in original (unencrypted) text
        decrypted_text = []
        for char in self.original_text.split(" "):
            if char == "0":
                decrypted_text.append(" ")
            else:
                try:
                    index = int(char) - 1
                except ValueError:
                    decrypted_text.append(char)
                else:
                    decrypted_text.append(INDEX_TO_LETTER_MAP[index])
        return "".join(decrypted_text)
