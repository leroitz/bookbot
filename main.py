
def main():
    with open("books/frankenstein.txt") as f:
        return f.read()

def number_of_words():
    text = main().split
    words = len(text())
    return words

numbers = number_of_words()

def count_characters():
    text= main().lower()
    dictionary_of_book= {}
    for i in text:
        dictionary_of_book[i] = dictionary_of_book.get(i,0) +1
    return dictionary_of_book

dictionary_of_book= {}
text= main().lower()

for i in text:
    dictionary_of_book[i] = dictionary_of_book.get(i,0) +1



message= f"""---Begin report of books/frankenstein.txt---/n
    {numbers} words found in a text
    
    dafadsf"""
def sort_on(dictionary_of_book):
    return dictionary_of_book[count_characters()]

dictionary= [dictionary_of_book]

dictionary.sort(reverse=True, key= sort_on)
print(dictionary)





    
  




















    