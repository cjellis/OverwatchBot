import nltk
import json
import decision_module
from nltk.stem.wordnet import WordNetLemmatizer
#################################################
keywords = []
normalize_list = {}
#################################################


def read_keywords():
    global keywords
    """
    Reads in the keyword file and stores them
    :return: 
    """
    with open('keywords_in_kb.json', 'r') as keys:
        data = json.load(keys)
        for key in data:
            keywords.append(key)


def load_normalized():
    global normalize_list
    """
    Reads in the file of normalizations and stores them
    :return: 
    """
    with open('normalized.json', 'r') as n:
        normalize_list = json.load(n)


def parse(input):
    """
    Normalizes, lemmatizes, tokenizes, and parses input
    :param input: comment from reddit or command line
    :return: a response to the input
    """
    # all input to lowercase
    input = input.lower()
    # normalize the input
    for key, value in normalize_list.items():
        if key in input:
            input = input.replace(key, value)

    # tokenize the input
    tokenized = nltk.word_tokenize(input)
    # lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

    # find keywords
    local_keywords = []
    for key in keywords:
        if key in lemmatized:
            local_keywords.append(key)
    return decision_module.generate_response(lemmatized, local_keywords)


def run():
    """
    Command line input
    :return: 
    """
    while True:
        user_input = str(input('What would you like to say? > '))
        if user_input == 'exit':
            break
        print(parse(user_input) + "\n")

read_keywords()
load_normalized()

if __name__ == "__main__":
    run()
