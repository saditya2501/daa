#Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	for j in range(n-1):
		for i in range(0, n-j-1):
			if arr[i] > arr[i+1] :
				arr[i], arr[i+1] = arr[i+1], arr[i]
arr = [56,85,15,2,6,89,7,3]

bubbleSort(arr)

print ("Sorted array is:")
for j in range(len(arr)):
	print ("%d" %arr[j]),
