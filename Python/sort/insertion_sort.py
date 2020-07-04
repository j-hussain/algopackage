# insertion_sort.py
# O(n^2)
def insertion_sort(list):
	for i in range(1, len(list)):
		initial_element = list[i]
		j = i-1
		while j >= 0 and list[j] > initial_element:
			list[j+1] = list[j]
			j -= 1
	return list

