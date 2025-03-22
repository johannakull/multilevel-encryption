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
