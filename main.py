def main():
    with open("books/frankenstein.txt") as f:
        return f.read()

def number_of_words():
    text = main().split
    words = len(text())
    return words

def count_characters():
    text= main().lower()
    dictionary_of_book= {}
    for i in text:
        dictionary_of_book[i] = dictionary_of_book.get(i,0) +1
    print(dictionary_of_book)



count_characters()





    