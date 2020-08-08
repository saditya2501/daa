# Python program for implementation of Selection
A=['t','u','t','o','r','i','a','l']
for i in range(len(A)):
    min = i
    for j in range(i + 1, len(A)):
        if A[min] > A[j]:
            min = j
    A[i], A[min] = A[min], A[i]
print("Sorted array is:-")
for i in range(len(A)):
    print( A[i]),
