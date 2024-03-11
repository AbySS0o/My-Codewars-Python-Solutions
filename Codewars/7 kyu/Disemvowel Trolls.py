def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    filtered_chars = []

    for char in string_:
        if char.lower() not in vowels:
            filtered_chars.append(char)

    filtered_string = ''.join(filtered_chars)
    return filtered_string