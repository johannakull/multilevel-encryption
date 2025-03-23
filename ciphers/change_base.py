from abc import ABC, abstractmethod


class ChangeBase(ABC):

    def __init__(self, base):
        self.base = base.upper()

    @abstractmethod
    def __repr__(self):
        return

    @abstractmethod
    def encrypt(self):
        return

    @abstractmethod
    def decrypt(self):
        return
