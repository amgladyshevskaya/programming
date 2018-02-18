#Вариант3
import random
def dict(fname1,fname2):
    dic={}
    with open(fname1,encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        for line in lines:
            words = line.split(';')
    with open(fname2,encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        for line in lines:
            clues = line.split(';')
    for word in words:
        for clue in clues:
            dic[clue]=word
    return dic

def guess(dic):
    keys = list(dic.keys())
    values = list(dic.values())
    key = random.choice(keys)
    print('Количество попыток:', len(key))
    print(key, ' ...')
    attempts = 0
    while len(key)>=attempts:
        guesss=input()
        if guesss == dic[key]:
            print('Правильно! ',key,'',guesss)
            break
        else:
            print ('нет!')
            attempts +=1
        
    
    
if __name__ == '__main__':
    guess(dict('words_1.csv','clues_1.csv'))
    
