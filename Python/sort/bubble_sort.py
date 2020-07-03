# bubble_sort.py
def bubble_sort(list):
	# O(n^2)
	arr_length = len(list)
	for i in range(len(arr_length)):
		# Flag to terminate code early if sorted
		sorted = True
		# Iterate between elements and compare values
		for j in range(arr_length - i - 1):
			if list[j] > list[j+1]:
				# Swap elements around
				list[j], list[j+1] = list[j+1], list[j]
				# Since we've had to make a swap, this suggests more needs sorting
			sorted = False

		if sorted:
			break

	return list