from ciphers.cipher import Cipher
from constants import LETTER_TO_INDEX_MAP, INDEX_TO_LETTER_MAP


class CaesarCipher(Cipher):

    def __init__(self, original_text: str):
        super().__init__(original_text)

    name = "Caesar Cipher"

    def _shift_chars(self, multiplier: int) -> str:
        while True:
            try:
                shift_number = int(input("Enter a shift number: ")) * multiplier
            except ValueError:
                print("Please enter an integer.")
            else:
                break
        shifted_text = []
        for char in self.original_text:
            if char in LETTER_TO_INDEX_MAP:
                i = LETTER_TO_INDEX_MAP[char]
                new_i = (i + shift_number) % len(LETTER_TO_INDEX_MAP)
                shifted_text.append(INDEX_TO_LETTER_MAP[new_i])
            else:
                shifted_text.append(char)
        return "".join(shifted_text)

    def encrypt(self) -> str:
        return self._shift_chars(1)

    def decrypt(self) -> str:
        return self._shift_chars(-1)
