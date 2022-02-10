import nltk
import math

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


def get_term_frequency(repetition: dict):
    number_words = len(repetition.keys())
    term_frequency = dict()

    for key in repetition:
        term_frequency[key] = repetition[key] / number_words

    return term_frequency


def init_downloads():
    nltk.download('gutenberg')
    nltk.download('punkt')
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')


def get_frequency_documents(files: list, repetition: dict) -> dict: 
    frequency_documents = dict() #number of documents the word appears by word

    for word in repetition:
        frequency_documents[word] = 0

    for file in files:
        words = nltk.corpus.gutenberg.words(file)
        for word in repetition:
            if(word in words):
                frequency_documents[word] += 1
    return frequency_documents


def calculate_idf(documents_number: int, frequency: int):
    logaritmando = (1 + documents_number) / (1 + frequency)
    idf = math.log10(logaritmando) + 1
    return idf


def get_inverse_document_frequency(documents_number: int, frequency_documents: dict):
    inverse_document_frequency = dict()

    for word in frequency_documents:
        inverse_document_frequency[word] = calculate_idf(documents_number, frequency_documents[word])
    
    return inverse_document_frequency


def calculate_tf_mult_idf(term_frequency: dict, inverse_document_frequency: dict):
    tf_mult_idf = dict()
    for word in term_frequency:
        tf_mult_idf[word] = term_frequency[word] * inverse_document_frequency[word]
        # print(f'tf= {term_frequency}; idf= f{inverse_document_frequency}; tf-idf= f{tf_mult_idf}' )
    return tf_mult_idf


def get_less_relevant(most_relevant_words: dict, term: str, frequency_term: float) -> str:
    for word in most_relevant_words:
        if(frequency_term > most_relevant_words[word]):
            return word
    return term


def get_most_relevant_words(tf_mult_idf: dict, most_number = 5):
    most_relevant_words = dict()

    for word in tf_mult_idf:
        if(len(most_relevant_words) < 5):
            most_relevant_words[word] = tf_mult_idf[word]
        
        less_relevant = get_less_relevant(most_relevant_words, word, tf_mult_idf[word])

        if(less_relevant != word): 
            most_relevant_words.pop(less_relevant)
            most_relevant_words[word] = tf_mult_idf[word]

    print(most_relevant_words)
    return most_relevant_words.values()


def main():
    init_downloads()
    files = ['austen-emma.txt', 'bible-kjv.txt', 'carroll-alice.txt', 'melville-moby_dick.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt']

    for file in files:
        repetition = get_amount_terms_repetition(file)
        term_frequency = get_term_frequency(repetition)

        frequency_documents = get_frequency_documents(files, repetition)
        inverse_document_frequency = get_inverse_document_frequency(len(files), frequency_documents)
        
        tf_mult_idf = calculate_tf_mult_idf(term_frequency, inverse_document_frequency)
        most_relevant_words = get_most_relevant_words(tf_mult_idf)
        print('Palavras mais relevantes: ', most_relevant_words)


if __name__ == "__main__":
    main()
