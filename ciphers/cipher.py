from abc import ABC, abstractmethod


class Cipher(ABC):

    def __init__(self, original_text):
        self.original_text = original_text.upper()

    @property
    @abstractmethod
    def name(self):
        return

    @abstractmethod
    def encrypt(self):
        return

    @abstractmethod
    def decrypt(self):
        return
