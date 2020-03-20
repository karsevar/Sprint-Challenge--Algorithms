#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) After running this problem in a repl and obtaining the
number of times the loop is run according to the specifications of the while loop (namely a < n _ n _ n),
I can say with confidence that the runtime complexity is O(n).
One can see that this answer is true because when ran with an n variable of 5 the termination value for the loop will be 125 and it will take a total of 5 iterations for a to be valued at 125.

Example count code:

```
def final_problem(n):
	a = 0
	loop_count = 0
	while a < n * n * n:
		loop_count += 1
		a = a + n * n
		print(a)

	print(loop_count)
	print(n*n*n)

print(final_problem(5))
```

b) From what I can see this algorithm's time complexity can be described as O(n _ n^1/2) in that there is an initial for loop that goes through the elements within the
range of n (example range(1, n+1), please keep in mind that the 0 value had to be
skipped to avoid an infinite loop) and the nested while loop only goes through half
of the range of n (as shown by the j _= 2 variable declaration). With all of that considered, when converted to the short hand of big(O) notation the actual run time complexity is O(n^2)

```
def first_question(n):
	sum = 0
	for i in range(1, n + 1):
		j = i
		while j < n:
			print(j)
			j *= 2
			sum += 1

```

c) After analyzing the number of times the following recursive function calls itself, I can say that the runtime complexity is simply O(n) since most recursive functions that only call themselves once usually have similar runtimes and that the n value (bunnies) is being incremented by minus one everytime the function calls itself.

Example of count code to which this answer is based:

```
def bunnyEars(bunnies, count=0):
	print('count', count)
	if bunnies == 0:
		return 0

	count += 1
	return 2 + bunnyEars(bunnies-1, count)
```

## Exercise II

create a variable called highest_floor (this variable will house the floor to which the first egg will break)

create a loop that will mirror the number of floors of the building in question (to keep confusion to a minimum the for loop will be written as for floor in range(1, floors+1)).

    within the loop add an if statement that checks if the egg breaks at that specific floor. If yes, add the floor value to the highest_floor variable and break out of the for loop. Else, continue the loop.

Return highest_floor.

Time Complexity: This algorithm will have a time complexity of O(n) because in the worst case the loop will have to go through all the floors if the highest_floor is the top floor.
