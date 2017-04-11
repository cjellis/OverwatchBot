import nltk
import json
import decision_module

keywords = []


def read_keywords():
    with open('keywords.json', 'r') as kb:
        data = json.load(kb)
        for key in data:
            keywords.append(key)


def parse(input):
    tokenized = nltk.word_tokenize(input)
    local_keywords = []
    for key in keywords:
        if key in tokenized:
            local_keywords.append(key)
    return decision_module.generate_response(tokenized, local_keywords)


def run():
    while True:
        input = str(raw_input('What would you like to say? >'))
        if input == 'exit':
            break
        print parse(input)


read_keywords()
if __name__ == "__main__":
    run()
