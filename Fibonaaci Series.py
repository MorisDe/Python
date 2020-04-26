def fib(x):
	a=0
	b=1
	n=0
	nterm=x
	while n < nterm:
		print(a)
		c=a+b
		a=b
		b=c
		n+=1

fib(10)