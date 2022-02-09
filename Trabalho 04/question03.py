import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def init_scores() -> dict:
    return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}


def analyzer_polarity(analyzer: SentimentIntensityAnalyzer, file: string) -> dict:
    scores = init_scores()
    file = open('utils/Question03/' + file, 'r')

    for line in file:
        score_line = analyzer.polarity_scores(line)
        for key, _ in score_line.items():
            scores[key] += score_line[key]
    
    return scores


def define_polarity(scores: dict):
    print('\nScores: ')
    print(scores)

    polarity = ''
    if(scores['compound'] > 0):
        polarity = 'Positivo'
    else: 
        polarity = 'Negativo'
    print('Polaridade: ' + polarity)


def main():
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

    scores_positive = analyzer_polarity(analyzer, 'positive_words.csv')
    scores_negative = analyzer_polarity(analyzer, 'negative_words.csv')

    define_polarity(scores_positive)
    define_polarity(scores_negative)


if __name__ == "__main__":
    main()
