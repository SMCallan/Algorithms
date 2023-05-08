'''
Let min = 0 and max = n-1.
If max < min, then stop: target is not present in array. Return -1.
Compute guess as the average of max and min, rounded down (so that it is an integer).
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
Otherwise, the guess was too high. Set max = guess - 1.
Go back to step 2.
'''
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 29, 35, 37]

def binary_search(arr, target):
	min = 0
	max = len(arr) - 1
	
	while min <= max: 
		guess_index = (min + max) // 2
		guess_value = arr[guess_index]
		
		if guess_value == target:
			print(guess_index)
			return guess_index
		elif guess_value < target:
			min = guess_index + 1
		else:
			max = guess_index - 1

	return -1
			
binary_search(arr, 29)


