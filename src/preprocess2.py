import os
import spacy

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
                    #target.write(c)
                    #c = source.read(1)
                    #print("eol hyphenation detected")
                    c = source.read(2)
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
            elif (c=='\n') :  # ignore line break
                target.write(" ")
                c = source.read(1)
            else :       # finally, regular characters are added to target
                target.write(c)
                c = source.read(1)
    source.close()
    target.close()



def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


def one_sentence_per_line(filename) :
    nlp = spacy.load('en')

    doc = nlp(open(filename,'r').read())

    out = ""

    for token in doc[:len(doc)-1] :         # last pb : no space after '-'
        if (token.is_sent_start) :
            out+= "\n"
        if (token.text != '\n') :
            if token.is_punct :
                out += token.text
            else :
                if (bool(len(out)) and out[-1] =='-') :   #no space
                    if (token.text in nlp.vocab) :
                        out += token.text
                    else :
                        out = out[:-1]
                        out += token.text
                else :
                    out += " " + token.text


    out += doc[len(doc)-1].text

    file = open(filename, 'w')
    file.truncate()
    file.write(out)
    file.close()





def extract_abstract() :
    files = os.listdir(txt_path)
    for file in files :
        if (file.endswith(".txt") and (os.exists("../data/abstract/"+str(file[:-4])+"_asbtract.txt") == 0)) :
            name = file[:-4] + "_abstract.txt"
            text = open(txt_path+file,'r').read()
            ab = text[text.index("Abstract")+8:min(text.index("\n1 "), text.index("Introduction"))]
            target = open(abstract+name,'w')
            target.write(ab)

"""
To do : take care of the words 'cut' with a " - "
Find a way to handle tags, maybe by creating a list of all important
tags that would give corresponding parts of the text a certain
weight.
"""
