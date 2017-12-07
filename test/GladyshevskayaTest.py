#Вариант2
#Задание1

with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
        if cells[2] == "гл":
            if cells[4] == "перех":
                print(line)

#Задание2

with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        cells = line.split()
        if cells[2] == "част":
            print(cells[0], end = ",")
            sum += float(cells[4])
print()
print(sum)

#Задание3
words = []
n = 0
word = input("Введите слово: ")
while word != "":
    word = input("Введите слово: ")
    n+=1
with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
    for i in range(n+1):
        if cells[0] == word:
            print(word, "IPM = ", cells[-1])
        

