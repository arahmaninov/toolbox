import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		print("START")
		f = func(*args, **kwargs)
		end = time.time()
		print("END")
		print(end - start)
	return wrapper



def foo():
	print("Ugabuga")

a = timer(foo)()

print(a)