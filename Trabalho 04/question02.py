import os
import nltk 

'''
Sobre a questão 02:
    Encontre as entidades nomeada presentes para o seguintes textos:
        
    i) apoloxi.txt
    ii) french-revolution.txt

    a) Qual é a quantidade de entidades "GPE" presentes em cada um dos texto?
    b) Qual é a quantidade de entidades "LOCATION" presentes em cada um dos texto?
    c) Qual é a quantidade de entidades "PERSON" presentes em cada um dos texto?
'''

def main():
    absolutePath = os.path.abspath("./")
    path = '/utils/Question02/'

    nameFile = ['apoloxi.txt', 'french-revolution.txt']

    for name in nameFile:
        analysisFile(name, absolutePath+"/Trabalho 04"+path+name)
    

def analysisFile(title, absolutePath):
    file = open(absolutePath, 'r')

    listTokens = list()

    print(">> Arquivo '{0}' <<".format(title))

    print("Quantidades SEM REPETIÇÕES !")

    entityWords = {'GPE': [], 'LOCATION': [], 'PERSON': []}

    for line in file:
        words = nltk.word_tokenize(line)
        sentTokenized = nltk.ne_chunk(nltk.pos_tag(words)) #unigramTagger.tag(words) 

        quantEntity(sentTokenized, entityWords)
    
    
    print("Quantidade de entidades 'GPE' : {0} ;".format(len(entityWords['GPE'])))
    print("Quantidade de entidades 'LOCATION' : {0} ;".format(len(entityWords['LOCATION'])))
    print("Quantidade de entidades 'PERSON' : {0} ;".format(len(entityWords['PERSON'])))

    print("\n------------------------------------\n")

    file.close()

def quantEntity(listTokens, entityWords):
   
    continuous_chunk = []
    current_chunk = []
    types = ['GPE','PERSON', 'LOCATION']

    for subtree in listTokens:
        if type(subtree) == nltk.Tree and subtree.label() in types:
            typeEntity = subtree.label()
            word = " ".join([token for token, pos in subtree.leaves()])

            if(word not in entityWords[typeEntity]):
                entityWords[typeEntity].append(word)



main()

