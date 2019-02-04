import string

def get_line():
    fin = open('origin.txt')
    line = fin.readline()
    d = {}
    for line in fin:
        process_line(line,d)
    check_frequent(d)
    return d

def process_line(line,d):
    line = line.replace('-', '')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        d[word] = d.get(word, 0) + 1
        
def check_frequent(d):
    new ={}
    length = input("enter the number of the frequent you want to check the word:")
    for key in d:
        if d[key] == length:
            new[key] = d[key]
    print (new)
    
get_line()