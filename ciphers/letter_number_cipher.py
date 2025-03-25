from ciphers.change_base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class LetterNumberCipher(ChangeBase):

    def __init__(self, base):
        super().__init__(base)

    name = "LetterNumber Cipher"

    def encrypt(self):
        encrypted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                new_char = ALPHABET.index(char) + 1
                encrypted_text += f"{new_char} "
            elif char == " ":
                encrypted_text += "0 "
            else:
                encrypted_text += f"{char} "
        return encrypted_text

    def decrypt(self):  # doesn't work if there are numbers in original (unencrypted) text
        decrypted_text = ""
        for char in self.base.split(" "):
            try:
                index = int(char) - 1
            except ValueError:
                decrypted_text += char
            else:
                if char == "0":
                    decrypted_text += " "
                else:
                    decrypted_text += ALPHABET[index]
        return decrypted_text
