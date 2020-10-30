def no_dups(s):
    # Your code here
    mydict = {v:i for i,v in enumerate(s.split())}
    rtn_string = []
    for k in mydict:
        rtn_string.append(k+" ")
    return "".join(rtn_string)[:-1]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))