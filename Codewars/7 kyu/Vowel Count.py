def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    vow_count = 0

    for i in sentence:
        if i.lower() in vowels:
            vow_count += 1

    return vow_count