def count_words(text):
    return len(text.split())

def count_chars(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_dict(dictionary):
    dict_list = []
    for value in dictionary:
        dict_list.append({"char": value, "num":dictionary[value]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]