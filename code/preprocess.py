source = open("article.xml",'r')
target = open("out.txt",'w')
c = source.read(1)
while c :
    if (c=='<') :              # skip the parts between <> for now
        while (c!='>') :
            c = source.read(1)
        c = source.read(1)
    else :
        if (c!='-') :
            target.write(c)
            c = source.read(1)
        else :                      # two cases :
            d = source.read(1)
            if (d!='\n') :          # 1) hyphenated terms
                target.write(c)
                target.write(d)
                c = source.read(1)
            else :                  # 2) end of line hyphenation
                c = source.read(1)

        if (c=='-') :
            d = source.read(1)
            if (d!='\n') :          # 1) hyphenated terms
                target.write(c)
                target.write(d)
                c = source.read(1)
            else :                  # 2) end of line hyphenation
                c = source.read(1)
        elif(c=='&') :

        else :       # regular characters
            target.write(c)
            c = source.read(1)



source.close()
target.close()


"""
To do : take care of the words 'cut' with a " - "
Find a way to handle tags, maybe by creating a list of all important
tags that would give corresponding parts of the text a certain
weight.
"""

# source = open("article.xml",'r')
#
# c = source.read(1)
#
# s = ""
#
# while(c) :
#     if (c=='-') :
#         c = source.read(1)
#         if (c=='\n') :
#             c = source.read(1)
#     s+=c
#     c = source.read(1)
#
# print(s)
