import string

def get_line():
    fin = open('origin.txt')
    line = fin.readline()
    d = {}
    for line in fin:
        process_line(line,d)
    check_frequent(d)
    return 

def process_line(line,d):
    line = line.replace('-', '')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        d[word] = d.get(word, 0) + 1
        
def check_frequent(d):
    new ={}
    for key in d:
        if d[key] > 1:
            new[key] = d[key]

    new_list = sorted(new.items(), key=lambda x:x[1])  
    for i in range (1, 20):
        print (new_list[-i])
    
print(get_line())