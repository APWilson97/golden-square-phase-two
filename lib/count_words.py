"""A function called count_words that takes a string as an argument
and returns the number of words in that string"""

def count_words(string):
    if string != str(string):
        raise Exception('Input should be a string!')
    elif string == '':
        return 0

    string_list = string.split(' ')
    if len(string_list) == 1:
        return 1
    
    list_of_words = []
    for word in string_list:
        if word.isalpha():
            list_of_words.append(word)
    
    return len(list_of_words)