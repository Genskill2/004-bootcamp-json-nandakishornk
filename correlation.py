# Add the functions in this file


def load_journal(fname):
	with open(fname,"r") as json_file:
		data=json.load(json_file)
	return data
	



