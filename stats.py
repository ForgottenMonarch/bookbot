def counting_words(book_string):
    sep_words = book_string.split()
    num_words = len(sep_words)
    print(f"Found {num_words} total words")

def counting_unique_characters(book_string):
    unique_chars ={}
    for char in book_string:
        lowercase_char = char.lower()
        if lowercase_char not in unique_chars:
            unique_chars[lowercase_char] = 1
        else:
            unique_chars[lowercase_char] += 1
    return unique_chars
def convert_dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    return char_list
def sort_on(items):
    return items["num"]
def sorts_chars(char_count_dict):
    converted_list = convert_dict_to_list(char_count_dict)
    converted_list.sort(key=sort_on, reverse=True)
    return converted_list


    