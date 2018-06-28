try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import spacy
import os
from segtok.segmenter import split_single, split_multi


def load_dico(dico_name) :
    dict = {}
    with open(dico_name) as dico :
        for word in dico :
            dict[str(word)[:-1]] = 1   # removes the '\n'
    return dict

def save_dico(dico, file_name) :
    with open(file_name,'w+') as output :
        for key in dico :
            output.write(key)
            output.write('\n')
        
def is_english(word, en_dictionnary, corpus_dictionnary = {}, min = 0) :
    
    if word.isalpha() :
        
        if word.lower() in en_dictionnary :
            
            return 1
            
        else :
            
            if word.lower() in corpus_dictionnary :
                
                if int(corpus_dictionnary[word.lower()]) > min :
                    
                    return 1
                    
                else :
                    
                    return 0
                    
            else :
                
                return 0
    
    else :
        
        i = len(word)
        j = 0
        
        while word[j].isalpha() == 0 :
            j += 1
        
        while (word[j:i].isalpha() == 0 and i >= j) :
            i-=1
            
        if (i==j) :
            
            return 0
        
        word = word[j:i]
        
        
              
        if word.lower() in en_dictionnary :
            
            return 1
            
        else :
            
            if word.lower() in corpus_dictionnary :
                
                if int(corpus_dictionnary[word.lower()]) >= min :
                    
                    return 1
                    
                else :
                    
                    return 0
                
def one_sentence_per_line(text) :
    sentences = split_single(text)
    output = '\n'.join(sentences)
    return output

def remove_empty_lines(text) :
    return(os.linesep.join([s for s in text.splitlines() if s]))
        
def last_word(string) :
    return string.split()[-1]
    
def first_word(string) :
    if string.split() : 
        return string.split()[0]
    else :
        return ""

def segment_sections(filename, to_keep = ["bodyText", "sectionHeader"]) :         # removes html tags, and adds new ones to segment the different sections

    output = ""
    
    tree = ET.ElementTree(file = filename)

    root = tree.getroot()

    for child in root.iter("algorithms") :
        for algo in child.iterfind("algorithm") :
            for elt in algo[0] :
                if (elt.tag in to_keep) :
                    if (elt.tag == "sectionHeader") :
                        output += ("<newSection>")
                    output += (elt.text)
                    
    return output

def format(text, en_dictionnary, corpus_dictionnary = {}, min = 1) :
    
    output = ""
    half = ""
    for old_line in text.split("\n") :
        # print(old_line)
        if old_line.endswith("-") :
            # print("hyphen detected")
            line = " ".join(old_line.split()[:-1])
        else :
            line = old_line
        
        if half != "":
            if (is_english(half+first_word(line), en_dictionnary, corpus_dictionnary, min)) :
                #print("english word")
                output += " " + half + line
            else : 
                # print(str(half+first_word(line)) + " is not an english word")
                #print("not an english word")
                output += " " + half + '-' + line
        else :
            output += " " + line
            
        
        if old_line.endswith("-") :
            half = last_word(old_line)[:-1]      
        else :
            half = ""
    
    return output
    
def preprocess_file(input_filename, output_filename, english_dictionnary_name, corpus_dictionnary_name = "", min = 1) :
    
    english_dico = load_dico(english_dictionnary_name)
    
    if corpus_dictionnary_name :
        
        corpus_dico = load_dico(corpus_dictionnary_name)
    
    text = segment_sections(input_filename)
    
    text = remove_empty_lines(text)
    
    text = format(text, english_dico, corpus_dico, min)
    
    text = one_sentence_per_line(text)
    
    with open(output_filename,'w+') as filehandle :
        filehandle.write(text) 

def load_dico(dico_name) :
    dict = {}
    with open(dico_name, 'r') as dico :
        for line in dico :
            line = line.split()
            if len(line) > 1 :
                dict[str(line[0])] = int(line[1])
            else :
                if len(line) == 1 :
                    dict[str(line[0])] = 1
                    
    return dict

def save_dico(dico, file_name) :
    with open(file_name,'w+') as output :
        for key in dico :
            output.write(key + " " + str(dico[key]))
            output.write('\n')

def augment_word_list(filename, word_list_name, en_dico_name) :
    
    nlp = spacy.load('en')

    if os.path.isfile(word_list_name) :
        dico = load_dico(word_list_name)
    else :
        dico = {}
        
    en_dico = load_dico(en_dico_name)
    
    print("reading file " + filename)
    doc = nlp(open(filename).read())
    for token in doc :
        if (token.is_punct==0 and token.text!='\n' and token.is_alpha and str(token.text).lower() not in en_dico) :
            if (str(str(token.text).lower()) not in dico) :
                dico[str(str(token.text).lower())] = 1
            else :
                dico[str(str(token.text).lower())] += 1

    save_dico(dico, word_list_name) 