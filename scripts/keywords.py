import json
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
#################################################
keywords = {}
#################################################
# Read in the the file
with open('tokens.json') as infile:
	tokens = json.load(infile)

# Create an array of all of the words used with a character
lemmatizer = WordNetLemmatizer()
for char, tokenlist in tokens.items():
	# there's another level of list here
	# that contains each sentence. this should be removed eventually
	keywords[char] = []
	for sentence in tokenlist:
		lemmatized = [lemmatizer.lemmatize(token) for token in sentence]
		stop = stopwords.words('english')
		keywords[char] += [token for token in lemmatized if token not in stop]

# TODO
# now count the frequency of each word, 
# and compute the inverse document frequency
# and then done.

# Print the words to a file
res = open("otherkeywords.json", "w")
res.write(json.dumps(keywords))
res.close()



