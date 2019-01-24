#probability is more useful than frequency
def probTable(t):
	for key in t:
		total=sum(t[key].values())
		for ikey in t[key]:	#for andar wala
			t[key][ikey]=t[key][ikey]/total


model=probTable(createtable(triningdata))#Hello world hello hello

def sampleNext(ctx, inp):	#users idiot so extract last 3 characters
	inp=inp[-4,:]
	print(ctx[inp])
	if inp in ctx:
		return max(ctx[inp].items(),key=lambda x: x[1])[0]	#max returns tuple therefo 0th element
	else:
		return " "# kuch to return krega so space


sampleNext(model, "Hello W")		#l=1.0 output l or max of probability

model= prob(create(load_file(data_file)))	#dat file is speech

sampleNext(model,"countr")	#'y' is output



