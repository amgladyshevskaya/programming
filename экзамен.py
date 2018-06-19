import re
import os

def get_files(filename):
    start_path = './news.zip/'
    for files in os.walk(start_path):
        print(files)
def find_match(files):
    doc_id = []
    title = []
    author = []
    created = []
    topic = []
    tagging = []
    for file in files:
        results1 = re.findall('<meta content [.*?] name='tagging'>',file)
        tagging = tagging.append(results1)
        results2 = re.findall('<title>[.*?]</title>',file)
        title  = titile.append(results2)
        results3 = re.findall('<meta content [.*?] name='docid'>',file)
        doc_id = doc_id.append(results3)
        results4 = re.findall('<meta content [.*?] name='author'>',file)
        author = author.append(results4)
        results5 = re.findall('<meta content [.*?] name='created'>',file)
        created = created.append(results5)
        results6 = re.findall('<meta content [.*?] name='topic'>',file)
        topic = topic.append(results6)

def main():
    get_files('news.zip')

if __name__ == "__main__":
    main()
