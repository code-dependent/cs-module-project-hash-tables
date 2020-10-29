    # '''
    #     0. create a dict.
    #     1. split string
    #     2. loop through the list
    #     3. if

    # '''
import re
import string
punc = [ '\"',':', ';', ',', '.', '-', '+', '=', "\\", '/', '|', '[', ']', '{', '}', '(', ')','*','^','&']
punc = set(punc)
print(string.ascii_lowercase)
def word_count(s):
    word_count = {}
    res = ""
    # Your code here
    # [^a-zA-Z \'$]^\'
    y = re.sub(r'[^a-zA-Z\' ]', ' ', s)
    # for c in s:
    #     if c not in punc:
    #         res +=c
    print(res)

    t = y.split()
    for i,word in enumerate(t):
        print(i," ",word.lower())
        if word.lower() not in word_count:
            word_count[word.lower()] = 0
        word_count[word.lower()] += 1
    return word_count
    # print(t[0] == t[-1], t[0])



if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the "emergency" broadcast network. This is only a test.'))