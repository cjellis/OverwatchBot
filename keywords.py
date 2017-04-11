import nltk
import json
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

keywords = {}

with open('tokens.json') as infile:
	tokens = json.load(infile)

lemmatizer = WordNetLemmatizer()
for char, tokenlist in tokens.items():
	# there's another level of list here
	# that contains each sentence. this should be removed eventually
	keywords[char] = []
	for sentence in tokenlist:
		lemmatized = [lemmatizer.lemmatize(token) for token in sentence]
		stop = stopwords.words('english')
		keywords[char] += [token for token in lemmatized if token not in stop]

# now count the frequency of each word, 
# and compute the inverse document frequency
# and then done.

res = open("keywords.json", "w")
res.write(json.dumps(keywords))
res.close



