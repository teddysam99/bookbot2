def num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    for character in text:
        lowered = character.lower()
        if lowered not in dict:
            dict[lowered] = 1
        else:
            dict[lowered] +=1
    return dict

def sorted_list(dict):
    main_dict = {}
    