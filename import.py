import csv
import json
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
			elif len(row[0].split()) > 1:
				damagekey = current_char + ",damage," + row[0].split()[0]
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + row[1].lower() + " damage."]
				damagekey = current_char + ",damage," + row[0].split()[1]
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + row[1].lower() + " damage."]
			else:
				damagekey = current_char + ",damage," + row[0]
				chars[damagekey.lower()] = [current_char + "'s " + row[0] + " does " + row[1].lower() + " damage."]

res = open("damageimport.json", "w")
res.write(json.dumps(chars, indent=4, sort_keys=True))
res.close