import string
def book_file_get_words():
    fin = open('origin.txt')
    line = fin.read()
    word_list = line.split()
    word_newlist = []
    for word in word_list:
        word = word.strip(string.punctuation + string.whitespace)
        word_newlist.append(word)
    
    list_to_set(word_newlist)
    return 


def word_list():
    fin_word = open('words.txt')
    line = fin_word.read()
    word_list = line.split()
    return list_to_set(word_list)
    
    
def list_to_set(list1):
    set_list = set(list1)

def set_operation(set1,set2):
    i = set1 & set2
    c = set1 | set2
    d = set1 - set2  
    print("The number of the typos words that in book:" + str(len(d)))
    print("The number of the words that common in the book and the words list:" + str(len(i)))


if __name__ == "__main__":
    set_book = book_file_get_words()
    set_word_list = word_list()
    set_operation(set_book, set_word_list)