from stats import num_words
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = get_book_text("books/frankenstein.txt")
    word_count = num_words(path)
    print(f"{word_count} words found in the document")
    print(count_characters(path))


main()