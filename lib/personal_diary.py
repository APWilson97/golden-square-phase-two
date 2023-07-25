# A function called make_snippet that takes a string as an argument
# and returns the first 5 words and then '...' if there are 
# more than that

def make_snippet(string):
    if string != str(string):
        raise Exception("Input must be a string!")
    
    list_of_words = string.split(" ")
    if len(list_of_words) > 5:
        first_five_words = ' '.join(list_of_words[0:5])
        dots = '...'
        return first_five_words + dots
    else:
        return string