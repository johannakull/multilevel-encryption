from ciphers.change_base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class CaesarCipher(ChangeBase):

    def __init__(self, base: str):
        super().__init__(base)
        self.shift_number = None

    def __repr__(self):
        return "Caesar Cipher"

    def _shift_chars(self, shift_number: int):
        self.shift_number = int(input("Enter a shift number: "))
        shifted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = (i + self.shift_number) % len(ALPHABET)
                shifted_text += ALPHABET[new_i]
            else:
                shifted_text += char
        return shifted_text

    def encrypt(self) -> str:
        return self._shift_chars(self.shift_number)

    def decrypt(self) -> str:
        return self._shift_chars(self.shift_number * -1)
