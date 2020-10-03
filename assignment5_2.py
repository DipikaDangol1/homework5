def bunny_ears(num_bunnies):
	if(num_bunnies)==0:
		return 0
	if (num_bunnies%2)==0:
		return bunny_ears(num_bunnies-1)+3
	else:	
		return bunny_ears(num_bunnies-1)+2
a=int(input("enter the number:"))
result=bunny_ears(a)
print(result)