from abc import ABC, abstractmethod

ALPHABET = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
ALPHABET_SET = set(ALPHABET)

class ChangeBase(ABC):

    def __init__(self, base):
        self.base = base
        self.cipher = None

    @abstractmethod
    def encrypt(self):
        return

    @abstractmethod
    def decrypt(self):
        return


class CaesarCipher(ChangeBase):

    def __init__(self, base: str, shift_number: int):
        super().__init__(base)
        self.shift_number = shift_number

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


original = "HELLO WORLD"
caesar = CaesarCipher(original, 3)
print(caesar.encrypt())

encrypted = "KHOOR ZRUOG"
caesar = CaesarCipher(encrypted, 3)
print(caesar.decrypt())
