import csv
import json
import re
from enum import Enum

class ImportState(Enum):
	INIT = 1
	CHAR = 2
	STANDBY = 3

with open('overwatch.csv', 'r') as f:
	reader = csv.reader(f)
	state = ImportState.INIT

	chars = {}
	current_char = ""

	for row in reader:
		if state == ImportState.INIT:
			state = ImportState.STANDBY
			continue
		elif state == ImportState.STANDBY:
			state = ImportState.CHAR
			current_char = row[0]
		elif state == ImportState.CHAR:
			if row[0] == '':
				state = ImportState.STANDBY
				continue

			damage = 'not do any' if row[1] == '' or row[1] == 'N/A' else row[1].lower()
			if len(row[0].split()) > 1:
				damagekey = re.sub('[()]', '', current_char + ",damage," + row[0].split()[0])
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + damage + " damage."]
				damagekey = re.sub('[()]', '', current_char + ",damage," + row[0].split()[1])
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + damage + " damage."]
			else:
				damagekey = re.sub('[()]', '', current_char + ",damage," + row[0])
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + damage + " damage."]

res = open("damageimport.json", "w")
res.write(json.dumps(chars, indent=4, sort_keys=True))
res.close