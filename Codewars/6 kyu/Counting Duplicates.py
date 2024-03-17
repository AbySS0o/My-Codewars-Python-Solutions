def duplicate_count(text):
    new_list = []
    duplicates = []

    text = text.lower()

    for char in text:
        if char not in new_list:
            new_list.append(char)
        elif char in new_list:
            if char not in duplicates:
                duplicates.append(char)

    return len(duplicates)