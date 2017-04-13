import nltk
import json
import decision_module
from nltk.stem.wordnet import WordNetLemmatizer

keywords = []


def read_keywords():
    with open('keywords.json', 'r') as kb:
        data = json.load(kb)
        for key in data:
            keywords.append(key)

def load_normalized():
    with open('normalized.json', 'r') as n:
        data = json.load(n)
        return data

def parse(input):
    lemmatizer = WordNetLemmatizer()
    tokenized = nltk.word_tokenize(input)
    print(tokenized)
    tokenized = [token.lower() for token in tokenized]
    normalize_list = load_normalized()
    normalized = []
    print(normalized)
    for key, value in normalize_list.items():
        tokenized = [token.replace(key, value) for token in tokenized]
    normalized = tokenized
    print(normalized)
    local_keywords = []
    for key in keywords:
        if key in normalized:
            local_keywords.append(key)
    return decision_module.generate_response(normalized, local_keywords)


def run():
    while True:
        user_input = str(input('What would you like to say? >'))
        if user_input == 'exit':
            break
        print(parse(user_input))


read_keywords()
if __name__ == "__main__":
    run()
