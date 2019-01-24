file_name="lyrics.txt"

def load_file(file_name):

	f=open(file_name,"r")	#read binary for rb
	content= f.read()
	f.close()
	return content

#load_file(lyrics.txt)

training_data=load_file(file_name)

def createTable(text,k=3):	#dictionary
	text=text.lower()
	T={}
	for i in range(len(text)-k):
		X=text[i:i+k]
		Y=text[i+k]
		if X in T:
			if Y in T[X]:	#dic k andar wale me dekho dict s.t. increase in freq karna h ya nai
				T[X][Y]+=1

			else:
				T[X][Y]=1
		else:			#if x name ki key nai hai then create
			T[X]={
				Y:1
			}
	return T
# createTable(training_data)
# training_data=load_file("lyr2.txt")
# createTable(training_data)
# training_data=load_file("lyr3.txt")
# createTable(training_data)



#probability is more useful than frequency
def probTable(t):
	for key in t:
		total=sum(t[key].values())
		for ikey in t[key]:	#for andar wala
			t[key][ikey]=t[key][ikey]/total
	return t

model=probTable(createTable(training_data))#Hello world hello hello
def sampleNext(ctx, inp):	#users idiot so extract last 3 characters
	inp=inp[-4:]
	if inp in ctx:
		return max(ctx[inp].items(),key=lambda x: x[1])[0]	#max returns tuple therefo 0th element
	else:
		return " "# kuch to return krega so space

sampleNext(model, "Why")		#l=1.0 output l or max of probabilit

sampleNext(model,"countr")	#'y' is output



def genText(ctx,inp,length=1000):
	text=inp
	for _ in range(length):
		text+=sampleNext(ctx,text[-3])
	return text

#print(model)
print(genText(model,"Why not me"))	#university me answers predict
