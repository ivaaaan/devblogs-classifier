import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

with open('posts.json', 'r') as json_file:
    data = json.load(json_file)

with open('other.json', 'r') as json_file:
    data = data + json.load(json_file)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

topics_stats = {}
for post in data:
    category = post["category"]
    if category in topics_stats:
        topics_stats[category] += 1
    else:
        topics_stats[category] = 1


def preprocess(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in stop_words]
    return words

# feature extraction
def features(text):
    words = preprocess(text)
    return {'contains({})'.format(word): True for word in words}

labeled_titles = [(post["title"], post["category"]) for post in data]

features_set = [(features(n), category) for (n, category) in labeled_titles]
train_set = features_set

classifier = nltk.NaiveBayesClassifier.train(train_set)

print(classifier.classify(features("Deep Multi-task Learning and Real-time Personalization for Closeup Recommendations")))
