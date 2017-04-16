import json
#################################################
keywords = []
#################################################
# Read in knowledge base and get all keywords
with open('kb.json', 'r') as kb:
    data = json.load(kb)
    for key, value in data.items():
        keys = key.split(",")
        for keyword in keys:
            if keyword not in keywords:
                keywords.append(str(keyword))

# Write the keywords to the file
with open('keywords_in_kb.json', 'w') as keys:
    keys.write(json.dumps(keywords))
