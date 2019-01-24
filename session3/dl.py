file_name="lyrics.txt"

def load_file(file_name):

	f=open(file_name,"r")	#read binary for rb
	content= f.read()
	f.close()
	return content

#load_file(lyrics.txt)

training_data="riya riya riya"

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

createTable(training_data)