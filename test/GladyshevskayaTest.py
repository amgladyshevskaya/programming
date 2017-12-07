#Вариант2

with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
        if cells[2] == "гл":
            if cells[4] == "перех":
                print(line)
