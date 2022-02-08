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

    print("Iniciando treinamento para analisar o texto .")
    print("Aguarde, isso pode demorar...")
    
    taggedSents = nltk.corpus.mac_morpho.tagged_sents() #
    unigramTagger = nltk.tag.UnigramTagger(taggedSents) # treinando comportamento de tagger

    for name in nameFile:
        analysisFile(name, absolutePath+"/Trabalho 04"+path+name, unigramTagger)
    

def analysisFile(title, absolutePath, unigramTagger):
    file = open(absolutePath, 'r')

    listTokens = list()

    print("Arquivo '{0}'".format(title))

    print("Iniciando...")

    print("Analisando tipo de cada palavra (isso pode demorar)...")

    for line in file:
        words = nltk.word_tokenize(line)
        sentTokenized = unigramTagger.tag(words) 

        listTokens += sentTokenized 
        break # Remover caso deseje analisar mais de um paragrafo
    
    print("Iniciando contagem de entidades do tipo 'gpe','location' e 'person'")    
    data = quantEntity(listTokens)

    print("Quantidade de entidades 'GPE' : {0} ;".format(data['gpe']))
    print("Quantidade de entidades 'LOCATION' : {0} ;".format(data['location']))
    print("Quantidade de entidades 'PERSON' : {0} ;".format(data['person']))

    file.close()


def quantEntity(listTokens):
    quantGpe = 0
    quantLocation = 0
    quantPerson = 0

    for t in listTokens:
        if(t[1] == 'GPE'):
            quantGpe += 1
        
        elif(t[1] == 'LOCATION'):
            quantLocation += 1
        
        elif(t[1] == 'PERSON'):
            quantPerson += 1    
                  
    return {'gpe': quantGpe, 'location': quantLocation, 'person': quantPerson}


main()

