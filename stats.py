def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars

def sort_on(item):
    return item["num"]

def get_sorted_list(dict):
    list = []
    for key, value in dict.items():
        list.append({ "char": key, "num": value })
    
    list.sort(reverse=True, key=sort_on)
    return list