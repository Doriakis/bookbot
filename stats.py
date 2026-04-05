def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        if char.isalpha(): # We only want to report on letters, not numbers or symbols
            sorted_list.append({"char": char, "count": count})
    
    # This sorts the list based on the "count" key in descending order
    sorted_list.sort(reverse=True, key=lambda d: d["count"])
    return sorted_list