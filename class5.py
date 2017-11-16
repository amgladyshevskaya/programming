#fname = r"C:\Users\student\Desktop\text.txt"
#print(fname)
#print("привет\nстрока")
#print("привет\tстрока")

"""
text = ""
f = open(fname)
text = f.read()
print(text)
f.close()



fname = "C:\\Users\\student\\Desktop\\text.txt"
print(fname)
with open(fname) as f:
    text=f.read()
print(text[:100])
lines = text.split("\n")
print(lines[:5])


fname = "C:\\Users\\student\\Desktop\\text.txt"
print(fname)
with open(fname) as f:
    text=f.read()
lines = text.split("\n")
for line in lines:
    words = line.split()
    for word in words:
        print(word)
    print()


fname = "C:\\Users\\student\\Desktop\\text.txt"
print(fname)
with open(fname) as f:
    text=f.read()
lines = text.split("\n")
text_el = []
for line in lines:
    words = line.split()
    text_el.append(words)
    for word in words:
        print(word)
    print()
print(text_el[-2:])
print(len(text_el))

"""

fname = "C:\\Users\\student\\Desktop\\text.txt"
print(fname)
with open(fname) as f:
    #text=f.read()
    lines = f.readlines()
print(lines)
print(len(lines))


