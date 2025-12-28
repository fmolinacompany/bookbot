def count_words(text):
    words = text.split()
    # Return a list of the words in the string, 
    # using sep as the delimiter string
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    dict_chars = {}
    for char in lower_text:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    return dict_chars

def sort_chars(char_counts):
    items = [{"char": ch, "num": cnt} for ch, cnt in char_counts.items()]
    items.sort(key=lambda item: item["num"], reverse=True)
    return items

def sort_on(count_chars):
    return count_chars.sort(reverse=True, key=sort_on)

