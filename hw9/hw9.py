#вариант3
#формы глагола программировать 
import re
def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        words = re.findall(r'[^\s!,.?":;0-9]+', text)
    return words
def verb_forms(words):
    forms = []
    for word in words:
        if re.search('программир(у(ю|ют|я)|ешь|е(м|те))|ова(л|в|ла|ло|ли|нн(ый|ая|ое|ые))',words):
            forms = forms.append(word)
    return forms
def main(verb_forms):
    print('Формы глагола: ',forms)

if __name__ == '__main__':
     main(verb_forms(open_file(input('Введите имя файла '))))
    

        
        
