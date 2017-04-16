import json
import random
from collections import OrderedDict
#################################################
knowledge = []
#################################################


def generate_response(tokenized_input, input_keywords):
    """
    Uses the keywords to determine a response
    :param tokenized_input: input normalized, tokenized, and lemmatized
    :param input_keywords: keywords from the input
    :return: a response to the input
    """
    for value in knowledge:
        keywords = value["keys"]
        responses = value["responses"]
        if all(key in input_keywords for key in keywords):
            r = random.randint(0, len(responses)-1)
            return responses[r]

    return "I do not know how to answer that"


def read_knowledge():
    """
    Reads the knowledge base into memory
    :return: 
    """
    with open('kb.json', 'r') as kb:
        data = json.load(kb, object_pairs_hook=OrderedDict)
        for keywords, responses in data.items():
            keys = keywords.lower().split(",")
            knowledge.append({"keys": keys, "responses": responses})

read_knowledge()
