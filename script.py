from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import word_tokenize
import os
import random

nltk.download('punkt')


class Sentiment(object):

    def get_response(self, query):
        question_words = ["what", "when", "why", "which", "who", "how", "whose", "whom", "?"]
        query = query.lower()
        word_token = word_tokenize(query)
        positive_list = ['Sure', 'Thanks', 'Welcome', '(y)', ':)', 'Lol', 'Thank You']
        negative_list = ['Sorry', 'No', ':(', 'Nope', 'OK', 'Thanks']
        neutral_list = ['OK', 'Sure', 'Maybe', 'Thanks', 'Thank you', ':)', ';)']
        interrogative_list = ['Yes', 'No', 'Maybe', 'Sure', 'Thank You']
        flag = 0
        for q in word_token:
            if q not in question_words:
                flag = 0
            else:
                flag = 1
                break
        if flag == 1:
            print("Interrogative")
            return random.sample(interrogative_list, 4)

        else:
            analyser = SentimentIntensityAnalyzer()
            def print_sentiment_scores(sentence):
                snt = analyser.polarity_scores(sentence)
                temp = snt['compound']
                if temp > 0:
                    print("Positive")
                    return random.sample(positive_list, 4)
                elif temp == 0:
                    print("Neutral")
                    return random.sample(neutral_list, 4)
                else:
                    print("Negative")
                    return random.sample(negative_list, 4)
            return print_sentiment_scores(query)