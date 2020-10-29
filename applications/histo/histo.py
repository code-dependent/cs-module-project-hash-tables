# Your code here
'''
0. create a dict
1. loop through the file

    2. if word in file is not in the word_count.dict()
        add it as the key with the value 1
    else,
        increment word_count[word]+=1

'''
import re
def histo(file):

    string = ''
    word_count = {}

    with open("/Users/joshua/Desktop/CS_FLEX/modules/cs-module-project-hash-tables/applications/histo/robin.txt") as f:
        for line in f:
            string+=line
    f.close()

    string = re.sub(r'[^a-zA-Z\' ]', ' ', string)
    word_list = string.split()

    for word in word_list:
        w = word.lower()

        if w not in word_count:
            word_count[w] = ""

        word_count[w] +='#'

    a = list(word_count.items())
    a.sort(key=lambda tup: (-len(tup[1]), tup[0]))

    word_count = dict(a)
    for pat in word_count:
        print(f"{pat:15} {word_count[pat]}")

histo('dd')