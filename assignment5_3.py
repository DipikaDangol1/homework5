import time
def timeit(method):
	def timed(*args,**kw):
		start =time.time()
		result=method(*args, **kw)
		end=time.time()
		elapsed_time=start-end
		print(f"Finished {method.__name__!r} in {elapsed_time:.4f} secs")
		return result
	return timed

@timeit
def run(num):
	for i in range(num):
		sum=i*2;
		print(sum)
run(10)