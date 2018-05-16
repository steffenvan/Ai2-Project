import os

def preprocess(inputxml, outputtxt) :  # takes bracketted file names as arguments

    source = open(inputxml,'r')
    target = open(outputtxt,'w')
    c = source.read(1)
    while c :
        if (c=='<') :              # skip the parts between <> for now
            while (c!='>') :
                c = source.read(1)
            c = source.read(1)
        else :

            if (c=='-') :
                d = source.read(1)
                if (d!='\n') :          # 1) hyphenated terms
                    target.write(c)
                    target.write(d)
                    c = source.read(1)
                else :                  # 2) end of line hyphenation
                    c = source.read(1)
            elif(c=='&') :              # special xml characters
                next2 = source.read(2)
                if (next2 == 'lt') :
                    target.write('<')
                elif (next2 == 'gt') :
                    target.write('>')
                elif (next2 == 'am') :
                    target.write('&')
                elif (next2 == 'ap') :
                    target.write("\'")
                else :
                    target.write("\"")

                c = source.read(1)

                while (c!=";") :
                    c = source.read(1)
                c = source.read(1)
            else :       # finally, regular characters are added to target
                target.write(c)
                c = source.read(1)
    source.close()
    target.close()

preprocess("article.xml", "output.txt")

def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

remove_empty_lines("output.txt")

"""
To do : take care of the words 'cut' with a " - "
Find a way to handle tags, maybe by creating a list of all important
tags that would give corresponding parts of the text a certain
weight.
"""
