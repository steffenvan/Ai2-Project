import spacy

noisy_pos_tags = ["IN"]

nlp = spacy.load("en")

document = nlp('Part-of-speech tags are the properties of the word that are defined by the usage of the word in the grammatically correct sentence. These tags can be used as the text features in information filtering, statistical models, and rule based parsing.')

#print(dir(document))

# for token in doc :
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_, token.is_alpha, token.is_stop)

# for i in range(0,2) :
#     print(list(document.sents)[i])   # accessing each sentence of the text

tags = [str(w).upper() + " | tag : " + str(w.tag_)  + " | pos : " + str(w.pos_) for w in document]

for elt in tags :
    print(elt)


# function to detect noisy tokens :

def isNoise(token) :
    if token.pos_ in noisy_pos_tags :
        return True
    else :
        return False
