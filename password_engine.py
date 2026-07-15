from abc import ABC, abstractmethod
import random
import string
from custom_exception import InvalidLengthError


class PasswordGenerator(ABC):

    def __init__(self, length):
        if length < 4:
            raise InvalidLengthError(
                "Length must be at least 4."
            )
        self.length = length

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def validate_strength(self):
        pass


class NumericPinGenerator(PasswordGenerator):

    def __init__(self, length):
        super().__init__(length)

    def generate(self):
        return "".join(
            random.choice(string.digits)
            for _ in range(self.length)
        )

    def validate_strength(self):
        return self.length >= 4

    def __str__(self):
        return f"Numeric PIN Generator ({self.length} digits)"


class MemorablePassphraseGenerator(PasswordGenerator):

    def __init__(self, length):
        super().__init__(length)

        self.words = [
            "apple",
            "river",
            "tiger",
            "cloud",
            "green",
            "ocean",
            "python",
            "coffee",
            "happy",
            "future",
        ]

    def generate(self):
        return "-".join(
            random.choice(self.words)
            for _ in range(self.length)
        )

    def validate_strength(self):
        return self.length >= 3

    def __str__(self):
        return (
            f"Memorable Passphrase Generator "
            f"({self.length} words)"
        )


def batch_generate(generators):
    for generator in generators:
        print(generator)
        print("Generated:", generator.generate())
        print("-" * 40)