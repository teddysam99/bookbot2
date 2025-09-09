def num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    text = text.lower()
    for letter in text:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter]+=1
    return dict