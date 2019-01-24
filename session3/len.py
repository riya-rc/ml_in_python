def genText(ctx,inp,length=1000):
	text=inp
	for _ in range(length):
		text+=sampleNext(ctx,text[-3])
	return text


gentext(model,"my dear")	#university me answers predict