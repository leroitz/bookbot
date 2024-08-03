def main():
    book_path = "books/frankenstein.txt"
    text= get_book_text(book_path)
    amount_of_words = text_from_book(text)
    strings_lower = count_characters(text)
    list_strings= [strings_lower]
    

    print(list_strings)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def text_from_book(text):
    words= text.split()
    count= len(words)
    return count

def count_characters(text):
    lowered_string = text.lower()
    clean_text= "".join(char for char in lowered_string if char.isalpha())
    dictionary_of_text= {}

    for i in clean_text:
        if i not in dictionary_of_text:
            dictionary_of_text[i] = 1
        
        
        else:
            dictionary_of_text[i] +=1
    return dictionary_of_text





main()

    
  




















    