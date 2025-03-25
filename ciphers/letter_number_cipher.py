from ciphers.change_base import ChangeBase
from constants import LETTER_TO_INDEX_MAP, INDEX_TO_LETTER_MAP


class LetterNumberCipher(ChangeBase):

    def __init__(self, base):
        super().__init__(base)

    name = "LetterNumber Cipher"

    def encrypt(self):
        encrypted_text = ""
        for char in self.base:
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
        for char in self.base.split(" "):
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
