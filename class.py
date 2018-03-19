'''
>>> s = 'abracadabra'
>>> 'abra' in s
True
>>> s.find('abra')
0
>>> import re
>>> results = re.findall('abra', s)
>>> results
['abra', 'abra']
>>> s
'abracadabra'
>>> results = re.findall('a.', s)
>>> results
['ab', 'ac', 'ad', 'ab']
>>> results = re.findall('a..',s)
>>> results
['abr', 'aca', 'abr']
>>> results = re.findall('A..',s)
>>> results
[]
. - любой символ

>>> results = re.findall('ab?', s)
>>> results
['ab', 'a', 'a', 'ab', 'a']
? - 1 or 0 times


>>> results = re.findall('ab+', s)
>>> results
['ab', 'ab']
>>> s += 'abbbabb'
>>> s
'abracadabraabbbabb'
>>> results
['ab', 'ab']
>>> results = re.findall('ab+',s)
>>> results
['ab', 'ab', 'abbb', 'abb']

+ - b 1 or more times


>>> results = re.findall('ab{2,3}', s)
>>> results
['abbb', 'abb']

>>> results = re.findall('ab{,2}', s)
>>> results
['ab', 'a', 'a', 'ab', 'a', 'abb', 'abb']
>>> results = re.findall('ab{2,}',s)
>>> results
['abbb', 'abb']


>>> re.findall('[a-zA-Z0-9_]+', sent) vse slova
re.findall("\w+",sent)

>>> sent = 'Программа развития – это стратегия создания на базе ВШЭ передового научно-образовательного, аналитического, консалтингового и проектного центра мирового класса.'
>>> re.findall('\w+',sent)
['Программа', 'развития', 'это', 'стратегия', 'создания', 'на', 'базе', 'ВШЭ', 'передового', 'научно', 'образовательного', 'аналитического', 'консалтингового', 'и', 'проектного', 'центра', 'мирового', 'класса']
>>> re.findall('\W+',sent)
[' ', ' – ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ', ', ', ', ' ', ' ', ' ', ' ', ' ', '.']
>>> re.findall('[.?!]+',sent)
['.']


import re
with open('cosmos.txt',encoding='utf-8') as f:
    text = f.read()
#results = re.findall("«[а-яА-ЯёЁ\d-]+»", text)
#results = re.findall("\d{1,2} [а-я]+ \d{4}", text)
#print(results)

match = re.search("\d{1,2} [а-я]+ \d{5}", text)
if match:
    print(match)
    
print(match.group())



'''
import re
with open('wiki.html', encoding='utf-8') as f:
    text = f.read()
page_title = re.findall('<title>(.*)<\title>', text)[0]
print(page_title)
























