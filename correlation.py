# Add the functions in this file
def load_journal(fname):
	f=open(fname,"r")
	dic=[dict()];
	cnt=0
	for i in f:
		dic[cnt]["events"]=i["events"]
		cnt=cnt+1
	f.close()
	return dic


