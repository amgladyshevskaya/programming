
'''
word = 'привет'
print (word)

for letter in word:
    print(letter)
    print('---')

for i in word:
    print(i)
    print(i*3)
print(i)

a = 0
for i in word:
    print(i,a)
    a += 1
print(a)

print('='*10)
#print(word[0])
print(len(word))
print(word[len(word)-1])
print(word[-4])

a=0
for letter in word:
    if a % 2 != 0:
        print(letter)
    a += 1
   
word = 'добрый_день!'
print(word)
#print(word[::-1])

part = word[3:6]
print(word[:3] + '!' + part +'!' + word[6:])

my_sum = 0
for i in range(3, 20, 2):
    
    print()
    print('i =',i)
    if i > 10 and i % 2 != 0:
        print( i**2)
    
    my_sum += i
    print(i, 'my_sum =', my_sum)
print(my_sum)
print('end.')


n = input('введите число: ')
n = int(n)

my_sum = 0
for i in range (n+1):
    my_sum += i
    print(i,'my_sum =', my_sum)
print(my_sum)
print('end')


i = 10
while i >= 5:
    print(i)
    i -=1
print('i=', i)



i = 2
while i**2 <= 100:
    print(i, i**2)
    i += 1
print("i = ", i)


print("hello",end=', ')
print('world!')
for i in range(10):
    print()
    print(i, end=', ')
    if i == 8:
        continue
    print(i**2)
print('end.')

for i in range(5):
    x = input('Введите слово: ')
    n = len(x)
    print(n)
'''
n = int(input('введите число')
        
for i in range(n):
        num = int(input('введите число')
        if num > 0:
                  print('больше нуля')
        elif:
                  print('меньше нуля')
        else:
                  print('ноль')
print('end.')
        
             

    
