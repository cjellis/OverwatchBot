import json
import pprint
from collections import OrderedDict

knowledge = []


def generate_response(tokenized_input, input_keywords):
    for value in knowledge:
        print value
        keywords = value["keys"]
        responses = value["responses"]
        if all(key in input_keywords for key in keywords):
            # TODO pick response randomly
            return responses[0]

    # TODO generic response/i dont know
    return "I do not know how to answer that"


def read_knowledge():
    with open('kb.json', 'r') as kb:
        data = json.load(kb)
        for keywords, responses in data.iteritems():
            keys = keywords.split(",")
            knowledge.append({"keys": keys, "responses": responses})

read_knowledge()
print pprint.pformat(knowledge)
print generate_response("", ["hanzo","is","bad","please","switch"])