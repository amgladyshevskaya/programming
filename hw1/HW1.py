#Вариант 3
a = input ("Введите число а: ")
b = input ("Введите число b: ")
c = input ("Введите число c: ")
a = int(a)
b = int(b)
c = int(c)
#Проверяем условие №3
if a % b == c:
    print ("Число a дает остаток c при делении на b")
else:
    print ("Остаток от деления a на b не равен числу c")
# Проверяем условие №4
if a*c + b == 0:
    print ("Число c является решением линейного уравнения ax+b=0")
else:
    print ("Число c не является решением линейного уравнения ax+b=0")
print ("End.")    
