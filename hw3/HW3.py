#Вариант№3
slovo = str(input('введите слово '))
slovo_rev = slovo[::-1]
print(slovo_rev)
for letter in slovo_rev:
    if not (letter == 'з' or letter == 'я'):
        print(letter);
        
