from password_engine import (
    NumericPinGenerator,
    MemorablePassphraseGenerator,
    batch_generate,
)
from custom_exception import InvalidLengthError

try:
    pin = NumericPinGenerator(6)

    phrase = MemorablePassphraseGenerator(4)

    generators = [pin, phrase]

    batch_generate(generators)

except InvalidLengthError as e:
    print(e)

finally:
    print("Program Finished.")