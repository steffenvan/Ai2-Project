import os
from preprocess_functions import *
from path import root

path = root + "data/"

class Article :

    def __init__(self, filename) :

        assert(os.path.exists(path + "xml/" + filename + ".xml")) , "No matching xml file has been found"
        self.xml = path + "xml/" + filename + ".xml"
        self.txt = path + "txt/" + filename + ".txt"
        self.json = path + "json/" + filename + ".json"

        print("now processing " + filename)

        if (os.path.exists(self.txt) == 0) :
            print("Creating text file from xml...")
            preprocess_file(self.xml, self.txt, path + "dico.txt", path + "corpus_words.txt", 2)
            print("Text file created.")
            augment_word_list(self.txt, path + "corpus_words.txt", path + "dico.txt")

        else :
            print("Text file already exists.")

        # if (os.path.exists(self.json) == 0) :
        #     command = "/Users/paulazoulai/Desktop/pre/semafor/bin/runSemafor.sh " + self.txt + " " + self.json + " 4"
        #     os.system(command)
        #     print("Json file created.")

        # else :
        #     print("Json file already exists.")
