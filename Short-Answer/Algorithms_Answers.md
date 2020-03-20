#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

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

c)

## Exercise II
