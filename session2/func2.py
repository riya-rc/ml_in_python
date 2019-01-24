def show(a,b,*args):
	print (a)
	print (args)

show(1,2,4,5)
#1
#(4,5)

def print(a,b,end='\n',sep=' ')

def s(*args,b):
	print(args)
	print(b)	#calling is almost impossible

#args baad me aata h positional ke

def s(a, *args,b=10,**kwargs):
	print(a)

s(1,2,3,4,name="ria")
#1
#(2,3,4)
#10
#{'name':"ria"}