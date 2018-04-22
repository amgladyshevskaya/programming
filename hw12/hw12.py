#Вариант3

import os
import re

def main():
    count = 0
    flist = os.listdir()
    for file in flist:
        if os.path.isdir(file):
            if re.match('^[а-яА-Я]', file):
                count += 1
    print(count)
            
if __name__ == '__main__':
    main()
    
