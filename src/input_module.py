import nltk
import json
import decision_module
from nltk.stem.wordnet import WordNetLemmatizer
#################################################
keywords = []
normalize_list = {}
#################################################


def read_keywords():
    """
    Reads in the keyword file and stores them
    :return: 
    """
    global keywords
    with open('keywords_in_kb.json', 'r') as keys:
        data = json.load(keys)
        for key in data:
            keywords.append(key)


def load_normalized():
    """
    Reads in the file of normalizations and stores them
    :return: 
    """
    global normalize_list
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

    # tokenize the input
    tokenized = nltk.word_tokenize(input)

    normalized = []
    # normalize the input
    for token in tokenized:
        if token in normalize_list.keys():
            normalized.append(normalize_list[token])
        else:
            normalized.append(token)
    # lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in normalized]

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
