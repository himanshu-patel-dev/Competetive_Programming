'''
Show the use of yield

The yield statement is only used when defining a generator 
function and is only used in the body of the generator function.

Using a yield statement in a function definition is sufficient to cause 
that definition to create a generator function instead of a normal function.

The yield statement suspends the function’s execution and sends a value back 
to the caller, but retains enough state to enable the function to resume where 
it is left off. When resumed, the function continues the execution immediately 
after the last yield run. This allows its code to produce a series of values 
over time rather them computing them all at once and sending them back like a 
list.
'''

def simpleGeneratorFunction():
	# use yield keyword in function to make convert normal 
	# function into generator funciton

	yield 1
	yield 2
	yield 3

def nextSquare1():
	# stopping is dependent on calling function
	i = 1

	while True:
		yield i*i
		i += 1

def nextSquare2():
	# stopping is dependent on generator function
	i = 1
	while True:
		if i*i > 100:
			return
		yield i*i
		i += 1

if __name__ == "__main__":


	for val in simpleGeneratorFunction():
		print(val)

	print('-'*20)
	lst = simpleGeneratorFunction()
	for val in lst:
		print(val)

	print('-'*20)
	for sq in nextSquare1():
		if sq > 100:
			break
		print(sq)

	print('-'*20)
	for sq in nextSquare2():
		print(sq)

	print('-'*20)
	# use of next in generator object, when called generator object returns 
	# a iterator object
	Iterator_obj = nextSquare1()
	print( next(Iterator_obj) )
	print( next(Iterator_obj) )
	print( next(Iterator_obj) )
