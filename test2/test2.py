#Вариант1
import re
def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text
def count_lines(text):
    k=0
    header = re.findall(r'<teiHeader>(.*)</teiHeader>',text)
    for line in header:
        k+=1
    return k

def write_result(k):
    with open('results.txt','w',encoding='utf-8') as f:
        f.write(str(k))

def main():
    write_result(count_lines(open_file('test.xml')))
if __name__ == "__main__":
    main()

        
    
    
        
