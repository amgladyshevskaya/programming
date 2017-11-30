"""
def hello():
    print("hello")
#вызываем функцию
hello()
#если не вызываем функцию, ничего не будет упс

#вводим переменную?
def hello(user):
    print("hello, " + user + "!")

hello("Sasha")


def hello(user1, user2, user3):
    print("hello, " + user1 + "!")
    print(user2.title())
    print(user3.title())

hello("Sasha","Poppy","Bob")



def hello(user1, age):
    print("hello, " + user1 + "!")
    if age > 10:
        print("older than 10")
    else:
        print(age)

hello("Sasha",18)



def hello(user1, age):
    print("hello, " + user1 + "!")
    if age > 10:
        print("older than 10")
    else:
        print(age)
    sum_ = 0
    for i in range(16):
        sum_ += 1
    print(sum_)
    print(gl)
   return user.title()

gl = 100
hello("Sasha",18)
print(sum_)






def hello(user1):
    #пиши че делает функция а то непонятноо
    print("hello, " + user1 + "!")
    return user1.title()
user_title = hello("ann")
print(user_title)



def elements(word):
    #печатает по букве на строчке, а потом кол-во символов
    for i in word:
        print(i)
    print(len(word))
elements("shrek")


def elements(word):
    #на вход список, печатаем длину списка
    for i in word:
        print(i)
    print(len(word))
sent = "shrek is love shrek is life"
els = sent.split()
elements(els)




def elements(word):
    for i in word:
        print(i)
    print(len(word))
def tokenize(sentence):
    words = sentence.split()
    return(words)

sent = "shrek is love shrek is life"
tok_result = tokenize(sent)
print(tok_result)

for w in tok_result:
    print(w.upper())




#берет на вход имя файла, открывает, читает и возвращает список слов

def lines_div(fname):
    with open(fname, encoding="utf-8") as f:
        lines_raw = f.readlines()
    lines = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            lines.append(clear_line)
    
    return lines
lines = lines_div("textS.txt")
print(lines)


"""

def lines_div(fname):
    """ открыть файл, прочесть , разделить на строки,
        вернуть минимальную длину строки в символах"""
    with open(fname, encoding="utf-8") as f:
        lines_raw = f.readlines()
    lines_lengths = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            print(len(clear_line),clear_line)
            lines_lengths.append(len(clear_line))
    
    return min(lines_lengths)
min_l = lines_div("textS.txt")
print(min_l)





















