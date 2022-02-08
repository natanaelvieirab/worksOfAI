from nltk.corpus import gutenberg

def main():
    listText = ["shakespeare-caesar.txt", "shakespeare-hamlet.txt","shakespeare-macbeth.txt"]

    for title in listText:
        words = gutenberg.words(title)
        sents = gutenberg.sents(title)

        avg = len(words)/len(sents)

        data = wordsInTheText(words)        

        print(">> Referente à "+title+" <<")

        print("Número total de palavras(COM REPETIÇÃO): {0}".format(len(words)))
        print("Número total de sentenças : {0}".format(len(sents)))
        print("Número total de palavras(SEM REPETIÇÃO): {0}".format(data['length']))
        print("Número total de palavras não repetidas: {0} ".format(data['smaller']))
        print("Número total de palavras repetidas: {0}".format(data['larger']))
        print("Média de palavras por sentenças: {:.4f}".format(avg))

        print("\n")

def wordsInTheText( words):
    i = 0
    wordsDict = dict()

    for word in words:
        
        value = wordsDict.get(word)
        
        if(value == None):
            wordsDict[word] = 1
        else:
            wordsDict[word] += value

    values = wordsDict.values()
    
    smaller = 0 #menor : número de repetições igual a 1 
    larger = 0 #maior : número de repetições maior que 1 

    for d in values:
        if(d == 1):
            smaller += 1
        else:
            larger += 1
    
    return {'length': len(values),'smaller' : smaller, 'larger': larger}



main()