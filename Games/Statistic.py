def statistic(A, i):
    # i is the statistic that we are looking
    pivot = A[i] # we are assigning the pivot to be an index greater than the pivot
    startPointer = 0
    endPointer = i + 1
    while startPointer < i:
        while endPointer < len(A) - 1:
            if A[startPointer] > A[endPointer]: # swap so now we get a smaller index to the left of the pivot
                temp = A[endPointer]
                A[endPointer] = A[startPointer]
                A[startPointer] = temp
            endPointer = endPointer + 1
        endPointer = i + 1
        startPointer = startPointer + 1
    print(A)
    if i > len(A)/2:
        min = A[i]
        for j in range(i, len(A)):
            if A[j] < min:
                min = A[j]
        return min
    elif i < len(A)/2:
        max = A[i-1]
        for j in range(0, i):
            if A[j] > max:
                max = A[j]
        return max


A = [4, 2, -8, -9, 4, 2]
print("The statistic 2 is: ")
print(statistic(A, 2))
