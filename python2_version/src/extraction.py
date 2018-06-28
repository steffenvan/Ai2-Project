<<<<<<< HEAD
from path import root
=======
>>>>>>> python2_version
import json


"""
This file allows the extracion of only specific sections of json / txt files
"""

def extract_text(frame, vocab = [], stopwords = [], punct = []) :      # given a frame, extract all the text from frameElements / spans
    tokens = []
    for fe in frame["annotationSets"][0]["frameElements"] :
<<<<<<< HEAD
        
        tokens += fe["spans"][0]["text"].split()
    
    tokens += frame["target"]["spans"][0]["text"]
    
    
        
    L = list(map(str.lower,list(set(tokens))))
    
    if len(stopwords+punct) :
        L = [elt for elt in L if elt not in stopwords+punct+list(" ")]    # remove stopwords / punctuation if specified 
        
    if len(vocab) :
        L = [elt for elt in L if elt in vocab]                            # only keep words from a specified vocabulary if specified
        
    return L
=======
        # print(fe["spans"][0]["text"])
        tokens += (fe["spans"][0]["text"]).split()
        # print(tokens)
    tokens += frame["target"]["spans"][0]["text"]
    print(tokens)
    
    
        
    # L = list(map(str.lower,list(set(tokens))))
    
    # if len(stopwords+punct) :
    #     L = [elt for elt in L if elt not in stopwords+punct+list(" ")]    # remove stopwords / punctuation if specified 
    # 
    # if len(vocab) :
    #     L = [elt for elt in L if elt in vocab]                            # only keep words from a specified vocabulary if specified
    # 
    # return L
>>>>>>> python2_version

def abstract_json(json_file) :                    # returns the part of the json semafor output correspounding to the abstract
    full_output = json.load(open(json_file))
    i = 0
    while ("Abstract" not in full_output[i]["tokens"]) : # or "abstract" not in full_output[i]["tokens"]
        i += 1
    beg = i
    while ("Introduction" not in full_output[i]["tokens"]) :
        i += 1
    end = i
    return full_output[beg:end]
    
    
def conclusion_json(json_file) :                  # file = path / filename
        full_output = json.load(open(json_file))
        i = 0
        while ("Conclusion" not in full_output[i]["tokens"] and "newSection" not in full_output[i]["tokens"]) :
            i += 1
        beg = i
        i += 1
        while ("newSection" not in full_output[i]["tokens"]) :
            i += 1
        end = i
        return full_output[beg:end]
        
def abstract_txt(txt_file) :
    full = open(txt_file).read().split('\n')
    i = 0
    while (("Abstract" not in full[i]) and ("ABSTRACT" not in full[i]) and ("abstract" not in full[i]) and ("<newSection>" not in full[i])) :
        i += 1
    beg = i
    i += 1
    while ("<newSection>" not in full[i]) :
        i += 1
    end = i
    return '\n'.join(full[beg:end])
    
def abstract_txt_string(txt) :
    full = txt.split('\n')
    i = 0
    while (("Abstract" not in full[i]) and ("ABSTRACT" not in full[i]) and ("abstract" not in full[i]) and ("<newSection>" not in full[i])) :
        i += 1
    beg = i
    i += 1
    while ("<newSection>" not in full[i]) :
        i += 1
    end = i
    return '\n'.join(full[beg:end])
    

    
def conclusion_txt(txt_file) :
        full = open(txt_file).read().split('\n')
        i = 0
        while (("Conclusion" not in full[i]) or ("<newSection>" not in full[i])) :
            i += 1
        beg = i
        i += 1
        while ("<newSection>" not in full[i]) :
            i += 1
        end = i
        return '\n'.join(full[beg:end])