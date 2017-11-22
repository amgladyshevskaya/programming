#Вариант3
let3 = 0
let1 = 0
with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    text = text.replace('.','').replace(',','').replace('"','').replace('?','').replace('!','').replace('«','').replace('»','').replace('–','')
lines = text.split()
for word in lines:
    if len(word)==3:
            let3+=1
    elif len(word)==1:
            let1+=1
print("let3 ", let3)
print("let1 ", let1)
if let1!=0:
    if let3>let1:
        print("Слов длины 3 больше, чем слов длины 1 в ",let3/let1,"раз")
    elif let1>let3:
        print("Слов длины 1 больше, чем слов длины 3")
    elif let1==let3:
        print("Количество слов длины 1 равно количеству слов длины 3")
elif let1==0:
    print("Слов длины 1 нет")

            


