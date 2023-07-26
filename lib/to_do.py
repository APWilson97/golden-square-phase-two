def check_for_to_do(text):
    if text == '':
        raise Exception('Text is empty')
       
    to_do = '#TODO'
    if to_do in text:
        return True
    else:
        return False