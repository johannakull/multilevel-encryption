from ciphers.change_base import ChangeBase
from constants import LETTER_TO_INDEX_MAP


class AtbashCipher(ChangeBase):

    def __init__(self, base: str):
        super().__init__(base)

    name = "Atbash Cipher"

    def _generate_atbash_text(self) -> str:
        atbash_text = ""
        for char in self.base:
            if char in LETTER_TO_INDEX_MAP:
                i = LETTER_TO_INDEX_MAP[char]
                atbash_text += LETTER_TO_INDEX_MAP[25 - i]
            else:
                atbash_text += char
        return atbash_text

    def encrypt(self) -> str:
        return self._generate_atbash_text()

    def decrypt(self) -> str:
        return self._generate_atbash_text()
