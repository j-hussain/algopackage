# merge_sort.py

def merge_sort(left, right):
	if len(left) == 0:
		return right
	if len(right) == 0:
		return left

