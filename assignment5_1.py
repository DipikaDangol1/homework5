def my_range(start,stop=None,step=None):
	if step==None:
		step=1
	i=start
	while i<stop:
		yield i
		i+=step
	
for i in my_range(0,5):
	print (i)



