from ciphers.change_base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class CaesarCipher(ChangeBase):

    def __init__(self, base: str):
        super().__init__(base)
        self.shift_number = input("Enter a shift number: ")

    def encrypt(self) -> str:
        encrypted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = (i + self.shift_number) % len(ALPHABET)
                encrypted_text += ALPHABET[new_i]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self) -> str:
        decrypted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = (i - self.shift_number) % len(ALPHABET)
                decrypted_text += ALPHABET[new_i]
            else:
                decrypted_text += char
        return decrypted_text
