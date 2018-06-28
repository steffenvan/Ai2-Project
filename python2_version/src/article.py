import os
from preprocess_functions import *
from extraction import abstract_txt
TXT = 0
TXT_ABS = 1
JSON = 0
JSON_ABS = 1



if JSON :
    TXT = 1
if JSON_ABS :
    TXT_ABS = 1


ai2_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
root = os.path.abspath(os.path.join(ai2_path, os.pardir))  
path = ai2_path + "/data/"

class Article :

    def __init__(self, filename) :

        assert(os.path.exists(path + "xml/" + filename + ".xml")) , "No matching xml file has been found"
        self.xml = path + "xml/" + filename + ".xml"
        self.txt = path + "txt/" + filename + ".txt"
        self.json = path + "json/" + filename + ".json"
        self.json_abs = path + "json_abs/" + filename + ".json"
        self.txt_abs = path + "txt_abs/" + filename + ".txt"

        print("now processing " + filename)

        if TXT and (os.path.exists(self.txt) == 0) :
            
            print("Creating text file from xml...")
            preprocess_file(self.xml, self.txt, path + "dico.txt", path + "corpus_words.txt", 2)
            print("Text file created.")
            augment_word_list(self.txt, path + "corpus_words.txt", path + "dico.txt")

        else :
            if TXT :
                print("Text file already exists.")

        if JSON and (os.path.exists(self.json) == 0) :
            # command = "/Users/paulazoulai/Desktop/pre_python2/semafor/bin/runSemafor.sh " + self.txt + " " + self.json + " 4"
            command = root + "semafor/bin/runSemafor.sh " + self.txt + " " + self.json + " 4"
            os.system(command)
            print("Json file created.")

        else :
            if JSON == 1 :
                print("Json file already exists.")
        
        
        if TXT_ABS and (os.path.exists(self.txt_abs) == 0) :
            
            if (os.path.exists(self.txt_abs) == 0) :
                print("Creating abstract text file from xml...")
                preprocess_file_abs(self.xml, self.txt_abs, path + "dico.txt", path + "corpus_words.txt", 2)
                print("Abstract text file created.")
                augment_word_list(self.txt_abs, path + "corpus_words.txt", path + "dico.txt")
                
            
        
                
        if JSON_ABS and (os.path.exists(self.json_abs) == 0) :
            
            # command = "/Users/paulazoulai/Desktop/pre_python2/semafor/bin/runSemafor.sh " + self.txt_abs + " " + self.json_abs + " 4"
            command = root + "/semafor/bin/runSemafor.sh " + self.txt_abs + " " + self.json_abs + " 4"
            os.system(command)
            print("Json abstract file created.")
            
