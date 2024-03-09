import re

def to_camel_case(text):
    words = re.split(r'[-_]', text)
    if words[0].islower():
        words = [word.capitalize() for word in words]
        words[0] = words[0].lower()
    else:
        words = [word.capitalize() for word in words]
    return ''.join(words)