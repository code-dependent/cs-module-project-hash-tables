import random

# Read in all the words in one go
with open("/Users/joshua/Desktop/CS_FLEX/modules/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

mydict = {}
# TODO: analyze which words can follow other words
# Your code here
w = words.split()
for i in range(len(w)-1):
    if w[i] not in mydict:
        mydict[w[i]] = list()
    mydict[w[i]].append(w[i+1])


# TODO: construct 5 random sentences
# Your code here

puncs = {punc for punc in ".?!"}

for i in range(5):
    start = random.choice(mydict[random.choice(w)])
    end = random.choice(mydict[random.choice(w)])

    while not start[0].isupper():
        if start[0] == "\"" and start[1].isupper():
            break
        start = random.choice(mydict[random.choice(w)])

    print(start, end=" ")

    while end[-1] not in puncs:
        if end[-1] == "\"" and end[-2] in puncs:
            break
        print(end, end=" ")
        end = random.choice(mydict[end])

    print(end)
    print("\n")
