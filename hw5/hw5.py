#Вариант3
i=0
word=str(input("Введите слово: "))
with open("text.txt","w",encoding="utf-8") as f:
    while word!="":
        f.write(word[i+1:len(word)]+"\n")
        word=str(input("Введите слово: "))
        i=i+1
