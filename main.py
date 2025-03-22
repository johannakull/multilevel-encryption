from abc import ABC, abstractmethod


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

    def __init__(self, base):
        super().__init__(base)

    def encrypt(self) -> str:
        return "encrypted string"

    def decrypt(self) -> str:
        return "decrypted string"


# base_string = "hello world"
# caesar = CaesarCipher(base_string)
# encrypted_base_string = caesar.encrypt()
#
# print(encrypted_base_string)
