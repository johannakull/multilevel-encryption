from ciphers.cipher import Cipher
from constants import LETTER_TO_INDEX_MAP


class CaesarCipher(Cipher):

    def __init__(self, original_text: str):
        super().__init__(original_text)
        self.shift_number = None

    name = "Caesar Cipher"

    def _shift_chars(self, multiplier: int):
        self.shift_number = int(input("Enter a shift number: ")) * multiplier
        shifted_text = ""  # do this as a list instead
        for char in self.original_text:
            if char in LETTER_TO_INDEX_MAP:
                i = LETTER_TO_INDEX_MAP[char]
                new_i = (i + self.shift_number) % len(LETTER_TO_INDEX_MAP)
                shifted_text += LETTER_TO_INDEX_MAP[new_i]
            else:
                shifted_text += char
        return shifted_text

    def encrypt(self) -> str:
        return self._shift_chars(1)

    def decrypt(self) -> str:
        return self._shift_chars(-1)
