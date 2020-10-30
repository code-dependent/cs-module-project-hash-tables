# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def cypher_cracker(filename):
    freq = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z']
    letter_freq = {char:0 for char in freq}

    string = ""
    with open(filename, 'r') as f:
        for i in f:
            string += i

    for char in string:
        big_char = char.upper()
        if big_char in letter_freq:
            letter_freq[big_char]+=1

    tup_list = list(letter_freq.items())
    tup_list.sort(key = lambda x: x[1],reverse=True)

    for index,tup in enumerate(tup_list):
        letter_freq[tup[0]] = freq[index]

    rtn = ""
    for char in string:
        if char in letter_freq:
            rtn+= letter_freq[char]
        else:
            rtn+= char

    print(rtn)
cypher_cracker("/Users/joshua/Desktop/CS_FLEX/modules/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt")


