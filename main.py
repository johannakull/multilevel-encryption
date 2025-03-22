from abc import ABC, abstractmethod

ALPHABET = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


class ChangeBase(ABC):

    def __init__(self, base):
        self.base = base

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

    def encrypt(self) -> str:
        encrypted_string = ""

        for char in self.base:
            # this is O(n), think about alternative implementations
            if char in ALPHABET:
                i = ALPHABET.index(char)
                new_i = i + self.shift_number
                if new_i > len(ALPHABET) - 1:
                    print(len(ALPHABET))
                    new_i -= len(ALPHABET)
                encrypted_string += ALPHABET[new_i]
            else:
                encrypted_string += char

        return encrypted_string

    def decrypt(self) -> str:
        return "decrypted string"


original_text = "HELLO WORLD"
caesar = CaesarCipher(original_text, 3)
print(caesar.encrypt())
