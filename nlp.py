import nltk
import json
from nltk.tokenize.treebank import TreebankWordTokenizer

tokenized = {}

json_data = open("results.json").read()
data = json.loads(json_data)
tokenizer = nltk.data.load("english.pickle")
treebank_word_tokenize = TreebankWordTokenizer().tokenize

for char, quotes in data.items():
	tokenized[char] = []
	for quote in quotes:
		quote_tokens = treebank_word_tokenize(quote)
		print(quote_tokens)
		tokenized[char].append(quote_tokens)

res = open("tokens.json", "w")
res.write(json.dumps(tokenized))
res.close