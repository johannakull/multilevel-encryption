from ciphers.base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class AtbashCipher(ChangeBase):

    def __init__(self, base: str):
        super().__init__(base)

    def generate_new_text(self):
        new_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = 25 - i
                new_text += ALPHABET[new_i]
            else:
                new_text += char
        return new_text

    def encrypt(self):
        return self.generate_new_text()

    def decrypt(self):
        return self.generate_new_text()
