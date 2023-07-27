# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
        self.text_without_vowels = ''

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                self.text_without_vowels += self.text[i]
            i += 1
        return self.text_without_vowels
