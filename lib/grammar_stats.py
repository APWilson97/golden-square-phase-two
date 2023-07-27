import math

class GrammarStats:
    def __init__(self):
        self.passed_checks = 0
        self.total_checks = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == '':
            self.total_checks += 1
            return False
        
        start_of_text = text[0]
        end_of_text = text[-1]
        punctuation = ['.', '!', '?']

        if start_of_text.upper() == start_of_text and end_of_text in punctuation:
            self.passed_checks += 1
            self.total_checks += 1
            return True
        else:
            self.total_checks += 1
            return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return math.ceil((self.passed_checks / self.total_checks) * 100)