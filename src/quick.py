from preprocess_functions import *

path = "../data/"

dico = load_dico(path + "dico.txt")

for word in dico :
    print(word + " " + str(dico[word]))