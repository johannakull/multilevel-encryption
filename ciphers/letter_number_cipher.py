from ciphers.cipher import Cipher
from constants import LETTER_TO_INDEX_MAP, INDEX_TO_LETTER_MAP


class LetterNumberCipher(Cipher):

    def __init__(self, original_text):
        super().__init__(original_text)

    name = "LetterNumber Cipher"

    def encrypt(self):
        encrypted_text = ""
        for char in self.original_text:
            if char in LETTER_TO_INDEX_MAP:
                new_char = LETTER_TO_INDEX_MAP[char]
                encrypted_text += f"{new_char} "
            elif char == " ":
                encrypted_text += "0 "
            else:
                encrypted_text += f"{char} "
        return encrypted_text

    def decrypt(self):  # doesn't work if there are numbers in original (unencrypted) text
        decrypted_text = ""
        for char in self.original_text.split(" "):
            if char == "0":
                decrypted_text += " "
            else:
                try:
                    index = int(char)
                except ValueError:
                    decrypted_text += char
                else:
                    decrypted_text += INDEX_TO_LETTER_MAP[index]
            return decrypted_text
