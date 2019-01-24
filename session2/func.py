def a(name):
	print("Hello",name)

a("riya")

a=10
def x():
	global a
	a=a+10
	print(a)

x()
print(a)

a=10
def x():
	a=20
	def y():	#closures func within func
		global  a
		a+=100
		print(a)
	y()
	print(a)

x()
print(a)	# 110 20 110

a=10
def x():
	a=20
	def y():	#closures func within func
		nonlocal  a		#goes to closest a
		a+=100
		print(a)
	y()
	print(a)

x()
print(a)	

def show(a,b=10,c=20):
	print(a,b,c)
show(1, c=100)
