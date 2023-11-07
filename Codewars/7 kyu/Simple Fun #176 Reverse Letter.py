def reverse_letter(string):
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string[::-1]

    