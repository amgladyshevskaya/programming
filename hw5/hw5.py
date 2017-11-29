i=0
word=str(input())
with open("text.txt","w",encoding="utf-8") as f:
    while word!="":
        f.write(word[i+1:len(word)]+"\n")
        word=str(input())
        i=i+1
