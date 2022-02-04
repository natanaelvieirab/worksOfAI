import nltk
from nltk.corpus import gutenberg
from nltk.text import Text

# todos os arquivos
#files = gutenberg.fileids()

listText = ["shakespeare-caesar.txt", "shakespeare-hamlet.txt","shakespeare-macbeth.txt"]

for title in listText:
    words = gutenberg.words(title)
    sentences = gutenberg.sent_tokenize(title)

    print(">> Referente à "+title+" <<")
    print("Número total de palavras: {0}".format(len(words)))
    print("Número total de sentenças : ", sentences)
    # print("Número total de palavras não repetidas: ")
    # print("Número total de palavras repetidas: ")
    # print("Média de palavras por sentenças: ")
    print("\n")
