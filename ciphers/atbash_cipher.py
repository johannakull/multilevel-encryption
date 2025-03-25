from ciphers.change_base import ChangeBase
from constants import ALPHABET, ALPHABET_SET


class AtbashCipher(ChangeBase):

    name = "Atbash Cipher"

    def __init__(self, base: str):
        super().__init__(base)

    def _generate_atbash_text(self) -> str:
        atbash_text = ""
        for char in self.base:
            if char in ALPHABET_SET:
                i = ALPHABET.index(char)
                atbash_text += ALPHABET[25 - i]
            else:
                atbash_text += char
        return atbash_text

    def encrypt(self) -> str:
        return self._generate_atbash_text()

    def decrypt(self) -> str:
        return self._generate_atbash_text()
