from cmath import log
import nltk

stopwords = []


def get_amount_terms_repetition(file):
    words = nltk.corpus.gutenberg.words(file)
    repetition = dict()

    for word in words:
        word = word.lower()

        if(word in stopwords):
            continue

        if(repetition.get(word)):
            repetition[word] += 1
        else:
            repetition[word] = 1

    return repetition


def get_term_frequency(repetition):
    number_words = len(repetition.keys())
    term_frequency = dict()

    for key in repetition:
        term_frequency[key] = repetition[key] / number_words

    return term_frequency

'''
def get_inverse_term_frequency(frequency_in_single_file):
    fields = nltk.corpus.gutenberg.fields()
    frequency_total = dict()

    for field in fields:
        frequency = get_term_frequency(field)

        for key,_ in frequency:
            if(frequency_total.get(key)):
                frequency_total[key] += frequency[key]
            else:
                frequency_total[key] = frequency[key]

    return 
'''

def init_downloads():
    nltk.download('gutenberg')
    nltk.download('punkt')
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')


def _create_documents_per_words(freq_matrix):
    word_per_doc_table = {}

    for sent, f_table in freq_matrix.items():
        for word, count in f_table.items():
            if word in word_per_doc_table:
                word_per_doc_table[word] += 1
            else:
                word_per_doc_table[word] = 1

    return word_per_doc_table


def calculate_tf_mult_idf(number_files):
    term_frequency = 0
    idf = log(1 + number_files, 1 + df(d, t))
    return term_frequency * idf

def main():
    init_downloads()
    files = ['austen-emma.txt', 'bible-kjv.txt', 'carroll-alice.txt', 'melville-moby_dick.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt']

    for file in files:
        repetition = get_amount_terms_repetition(file)
        term_frequency = get_term_frequency(repetition)
        print(term_frequency)

    # aplicate_TF_and_IDF()

    # Listem as 5 palavras mais relevantes de cada texto contido no corpus Gutemberg. 

# def main():
#     print(len(set(nltk.corpus.stopwords.words('english'))))
#     print(len(nltk.corpus.stopwords.words('english')))

if __name__ == "__main__":
    main()
