#Вариант 3
def filename():
    file_name = input('Введите имя файла ')
    return file_name

def read_file(file_name):
    with open (file_name, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split()
    return words

def word_list(words):
    wordlist = []
    for word in words:
        word = word.strip(',.()[]?!><-:;')
        wordlist.append(word)
    return wordlist

def hood_word(wordlist):
    hood = {}
    for word in wordlist:
        if word.endswith('hood'):
            if word in hood:
                hood[word] += 1
            else:
                hood[word] = 1
    return hood

def number(hood):
    if len(hood) > 0:
        print(str(len(hood)))
    else:
        print('no words with hood found')


def frequency(hood):
    values = list(hood.values())
    for key in sorted(hood, key=hood.get, reverse=True):
        if hood[key] == min(values):
            print(key)


def orig(hood):
    hood_keys = list(hood.keys())
    for element in hood_keys:
        print(element, '-', element[:-4])
    

def main():
    number(hood_word(word_list(read_file(filename()))))
    frequency(hood_word(word_list(read_file(filename()))))
    orig(hood_word(word_list(read_file(filename()))))
    
if __name__ == '__main__':
    main()
