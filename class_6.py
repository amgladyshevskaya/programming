'''
filename = "text.txt"
with open(filename, 'w') as f:
    f.write('hello')

sent = "доброе утречко страна"
words = sent.split()
with open('text.txt','w',encoding = 'utf-8')as f:
    f.writelines(words)


sent = "доброе утречко страна"
words = sent.split()
lines=[]
for w in words:
    lines.append(w+'\n')
with open('text.txt','w',encoding = 'utf-8')as f:
    f.writelines(lines)


sent = "доброе утречко страна"
words = sent.split()
lines=[]
for w in words:
    lines.append(w+'\n')
with open('text.txt','a',encoding = 'utf-8')as f:
    f.writelines(lines)


sent = "доброе утречко страна"
words = sent.split()
lines=[]
for w in words:
    lines.append(w+'\n')
with open('text.txt','w',encoding = 'utf-8')as f:
    for line in lines:
        f.write(line.upper())
sent = "доброе утречко страна"
words = sent.split()
lines=[]
for i in range(len(words)):
        if i%2!=0:
            lines.append(words[i].upper()+'\n')
        else:
            lines.append(words[i]+'\n')
with open('text.txt','w',encoding = 'utf-8')as f:
    f.writelines(lines)
        
'''
sent = "доброе утречко страна"
words = sent.split()
lines=[]
for w in words:
    lines.append(w+'\n')
with open('text.txt','w',encoding = 'utf-8')as f:
    for i,w in enumerate(words):
        print(i,w)
        if i%2==1:
            f.write(str(i)+' '+w.upper())
