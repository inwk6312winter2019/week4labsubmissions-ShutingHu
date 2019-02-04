import os
def sed(pattern,replacement,origin,words):
    fin = open(origin,'r')
    fout = open(words,'w')
    for line in fin:
        if pattern in line:
            new_line = line.replace(pattern,replacement)
            fout.write(new_line)
        else:
            fout.write(line)
        except:
            print('Something is Wrong !!!')
        fin.close()
        fout.close()
        if __name__ == '__main__':
            cwd = os.getcwd()
            print(cwd)
    pattern = 'of'
    replacement = 're'
    fin = 'origin.txt'
    fout = 'words.txt'
sed(pattern,replacement,origin,words)


