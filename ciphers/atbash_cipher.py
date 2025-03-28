from ciphers.cipher import Cipher
from constants import LETTER_TO_INDEX_MAP, INDEX_TO_LETTER_MAP


class AtbashCipher(Cipher):

    def __init__(self, original_text: str):
        super().__init__(original_text)

    name = "Atbash Cipher"

    def _generate_atbash_text(self) -> str:
        atbash_text = []
        for char in self.original_text:
            if char in LETTER_TO_INDEX_MAP:
                i = LETTER_TO_INDEX_MAP[char]
                atbash_text.append(INDEX_TO_LETTER_MAP[25 - i])
            else:
                atbash_text.append(char)
        return "".join(atbash_text)

    def encrypt(self) -> str:
        return self._generate_atbash_text()

    def decrypt(self) -> str:
        return self._generate_atbash_text()
