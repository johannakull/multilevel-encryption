from ciphers.base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class CaesarCipher(ChangeBase):

    def __init__(self, base: str):
        super().__init__(base)
        self.shift_number = input("Enter a shift number: ")

    def _shift_forward(self, index):
        new_index = index + self.shift_number
        if new_index > len(ALPHABET) - 1:
            new_index -= len(ALPHABET)
        return new_index

    def _shift_backward(self, index):
        new_index = index - self.shift_number
        if new_index < 0:
            new_index += len(ALPHABET)
        return new_index

    def encrypt(self) -> str:
        encrypted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = self._shift_forward(i)
                encrypted_text += ALPHABET[new_i]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self) -> str:
        decrypted_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                new_i = self._shift_backward(i)
                decrypted_text += ALPHABET[new_i]
            else:
                decrypted_text += char
        return decrypted_text
