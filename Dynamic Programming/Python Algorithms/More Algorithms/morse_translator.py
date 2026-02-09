# Morse translator

"""
Define a class called ”Morse translator” and implement the 
following functionality:

1. Define the init () method to accept one argument ”sequence”. 
    The ”sequence” is a string.Set this value within the body of the 
    class as ”self.sequence”.
2. Create a function called ”set” within the ”Morse translator” class. 
    The function should take a string ”sequence” as an argument. 
    Set this value within the body of the class as ”self.sequence”.
3. Create a function called ”get” within the ”Morse translator” class. 
    The function has no arguments and should return ”self.sequence” values.
4. Create a function called ”only small letters” within the 
    ”Morse translator” class. It should take no arguments. The function 
    should remove all non-letter characters from ”self.sequence” and 
    convert all uppercase letters into lowercase letters.
5. Create a function called ”translate” within the ”Morse translator” class. 
    It should take no arguments. The function should translate the string 
    ”self.sequence” after it has been executed with the function 
    ”self.only small letters”. The code should return the Morse code that 
    is equivalent to the string.
"""

class MorseTranslator:
    # Morse code dictionary for translation
    MORSE_CODE_DICT = {
        'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
        'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
        'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
        'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
        'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
        'z': '--..'
    }

    def __init__(self, sequence: str):
        """Initialize with a sequence."""
        self.sequence = sequence

    def set(self, sequence: str):
        """Set a new sequence."""
        self.sequence = sequence

    def get(self):
        """Get the current sequence."""
        return self.sequence

    def only_small_letters(self):
        """Remove non-letter characters and convert to lowercase."""
        self.sequence = ''.join(filter(str.isalpha, self.sequence)).lower()

    def translate(self):
        """Translate the sequence to Morse code."""
        # Ensure the sequence is processed to only lowercase letters
        self.only_small_letters()
        # Translate to Morse code
        morse_translation = ' '.join(self.MORSE_CODE_DICT[char] for char in self.sequence if char in self.MORSE_CODE_DICT)
        return morse_translation


# Example usage:
translator = MorseTranslator("Hello, World!")
print("Original Sequence:", translator.get())

translator.only_small_letters()
print("Processed Sequence:", translator.get())

morse_code = translator.translate()
print("Morse Code:", morse_code)

translator.set("Python 3.9!")
print("Updated Sequence:", translator.get())

morse_code = translator.translate()
print("Morse Code:", morse_code)

