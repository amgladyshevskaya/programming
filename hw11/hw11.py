#Вариант3
import re
def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text
def change_words(text):
    newtxt = re.sub('[яЯ]зык(\s|\W)','шашлык ',text)
    newtxt1 = re.sub('[яЯ]зыка(\s|\W)','шашлыка ',newtxt)
    newtxt2 = re.sub('[яЯ]зыку(\s|\W)','шашлыку ',newtxt1)
    newtxt3 = re.sub('[яЯ]зыком(\s|\W)','шашлыком ',newtxt2)
    newtxt4 = re.sub('[яЯ]зыке(\s|\W)','шашлыке ',newtxt3)
    newtxt5 = re.sub('[яЯ]зыки(\s|\W)','шашлыки ',newtxt4)
    newtxt6 = re.sub('[яЯ]зыков(\s|\W)','шашлыков ',newtxt5)
    newtxt7 = re.sub('[яЯ]зыкам(\s|\W)','шашлыкам ',newtxt6)
    newtxt8 = re.sub('[яЯ]зыками(\s|\W)','шашлыками ',newtxt7)
    newtxt9 = re.sub('[яЯ]зыках(\s|\W)','шашлыках ',newtxt8)
    
    return newtxt9

def write_result(newtxt9):
    with open('newfile.txt','w',encoding='utf-8') as f:
        f.write(newtxt9)
def main():
    write_result(change_words(open_file('Лингвистика.html')))
if __name__ == '__main__':
    main()
    
