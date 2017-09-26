"""
num = input ("Введите число:")

num = int(num)

num2 = input ("Введите второе число")

num2 = int(num2)
#word_length = len(word)

if num > 0:
    print(num)
    print ("Больше нуля")
else:
    print ("Не больше нуля")
    if num > -2:
        print ("Больше -2")
    else:
        print ("Не больше -2")
    #num = num + 100
    #num += 100
print(num)
print("End")
if num > 0 or num <=5:
    print(num, "Строго больше нуля ИЛИ меньше или равно 5")

print("End.")


if not 2< 3:
    print ("hello")
else:
    print( "nooo")

print("end")

if num % 2 == 0 and num2 % 2 == 0:
    print ("Оба числа четные")
elif  num % 2 == 0 and num2 % 2 != 0:
    print ("Первое - четное")
elif num % 2 != 0 and num2 % 2 ==0:
    print (" Второе - четное")
print( "END.")


x = input("Введите число:")
x = int(x)
print(x)

if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)
print( "END.")
"""
x = input ("Введите год:")
if len(x) != 4:
    print("Введите четырехзначное число")
else:
    x = int(x)
    print(x)

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("Високосный")
else:
    print("Невисокосный")




