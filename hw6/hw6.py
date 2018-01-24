#Вариант 3
#утвердительные, вопросительные, отрицательные, условные, побудительные

import random

def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        return words

def subj():
    nouns = open_file('subj.txt')
    return random.choice(nouns)


def verb(trans):
    trans_verbs = open_file('trans_vb.txt')
    intrans_verbs = open_file('intrans_vb.txt')
    if trans == 'tr':
        return random.choice(trans_verbs)
    return random.choice(intrans_verbs)


def imp(trans):

    trans_imperative = open_file('trans_imp.txt')
    intrans_imperative = open_file('intrans_imp.txt')
    if trans == 'tr':
        return random.choice(trans_imperative)
    return random.choice(intrans_imperative)


def obj_phrase(gen):
    m_adj = open_file('m_adj.txt')
    f_adj = open_file('f_adj.txt')
    n_adj = open_file('n_adj.txt')
    m_obj = open_file('m_obj.txt')
    f_obj = open_file('f_obj.txt')
    n_obj = open_file('n_obj.txt')
    if gen == 'm':
        adj = random.choice(m_adj)
        obj = random.choice(m_obj)
        return adj + ' ' + obj
    elif gen == 'f':
        adj = random.choice(f_adj)
        obj = random.choice(f_obj)
        return adj + ' ' + obj
    elif gen == 'n':
        adj = random.choice(n_adj)
        obj = random.choice(n_obj)
        return adj + ' ' + obj

#утвердительное
def sen1():
    a = random.choice([1,2,3,4]) #разные типы утвердительных предложений
    if a == 1:
        return subj() + ' ' + verb('tr') + ' ' + obj_phrase('m') 
    elif a == 2:
        return subj() + ' ' + verb('tr') + ' ' + obj_phrase('f')
    elif a == 3:
        return subj() + ' ' + verb('tr') + ' ' + obj_phrase('n') 
    else:
        return subj() + ' ' + verb('') 

#отрицательное
def sen2():
    a = random.choice([1,2,3,4]) #разные типы отрицательных предложений
    if a == 1:
        return subj() + ' ' + 'не' + ' ' + verb('tr') + ' ' + obj_phrase('m')
    elif a == 2:
        return subj() + ' ' + 'не' + ' ' + verb('tr') + ' ' + obj_phrase('f') 
    elif a == 3:
        return subj() + ' ' + 'не' + ' ' + verb('tr') + ' ' + obj_phrase('n')
    else:
        return subj() + ' ' + 'не' + ' ' + verb('')

#условное
def sen3():
    a = random.choice([1,2,3,4]) #разные типы условных предложений
    if a == 1:
        return 'если ' + sen1() + ', то ' + sen1() 
    elif a == 2:
        return 'если ' + sen1() + ', то ' + sen2() 
    elif a == 3:
        return 'если ' + sen2() + ', то ' + sen1() 
    else:
        return 'если ' + sen2() + ', то ' + sen2()
    
#побудительное
def sen4():
    a = random.choice([1,2,3,4])
    if a == 1:
        return subj() + ', ' + imp('tr') + ' ' + obj_phrase('m') + '!'
    elif a == 2:
        return subj() + ', ' + imp('tr') + ' ' + obj_phrase('f') + '!'
    elif a == 3:
        return subj() + ', ' + imp('tr') + ' ' + obj_phrase('n') + '!'
    else:
        return subj() + ', ' + imp('') + '!'
    
#вопросительное
def sen5():
    a = random.choice([1,2,3]) #разные типы вопросительного предложения
    if a == 1:
        return sen1() + '?'
    if a == 2:
        return sen2() + '?'
    if a == 3:
        return sen3() + '?'
    
def main():
    sen = [1,2,3,4,5]
    random.shuffle(sen)
    for i in range(5):
        if sen[i] == 1:
            print(sen1().capitalize() + '.', end=' ')
        elif sen[i] == 2:
            print(sen2().capitalize() + '.', end=' ')
        elif sen[i] == 3:
            print(sen3().capitalize() + '.', end=' ')
        elif sen[i]== 4:
            print(sen4().capitalize(), end=' ')
        else:
            print(sen5().capitalize(), end=' ')
            
if __name__ =="__main__":
    main()







