#Вариант3
import re

def open_file(filename):
     with open(filename, encoding='utf-8') as f:
        text = f.read()
     return text
def search(text):
    match = re.search('data-wikidata-property-id="P571">.*?([0-9]+)',text)
    date = match.group(1)
    return date

def add(date):
    with open('date.txt','w', encoding='utf-8') as f:
        f.write(date)
def main():
    add(search(open_file('вшэ.html')))
if __name__ == "__main__":
    main()
    
