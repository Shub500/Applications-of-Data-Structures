'''
Name: Shubham Mohole
Program: I realized that the i statistic can be found much easier by sorting the array and then finding the j-1 element
in the list because the i statistic and the indices are offseted by 1. The statistic function first calls quicksort which
sets the last index as the pivot value. Of course there is a chance if the last element was either the smallest or largest element
that we would have the worst case of quicksort which can be mitigated with a randomized quicksort that chooses an element
from inside the list and then swaps it with the last element. For efficiency we will use the randomized version so that our
expected run time is O(n lg n). The randomized quicksort swaps the pivot and the last element so that now the pivot is
at the last index. Then it partitions the array into four subarrays: the values less or equal to the pivot, the values greater than
the pivot, the unrestricted values, and the key itself. Then we put the pivot value in index right after the end of the
smaller value subarray. Finally, we recurse again on the subarrays until we have a sorted list.

'''

import random
def statistic(A,j):
    '''

    :param A: the list that will be used to find the statistic
    :param j: the statistic
    :return: returns the statistic
    '''
    if len(A) == 0: # input checks
        return "List was empty"
    if j <= 0:
        return "Invalid statistic entered"
    list = RandomizedQuicksort(A, 0, len(A) - 1) # sets the low and high indices for a sorting
    statistic = list[j-1] # because of the offset with the 1th statistic corresponding to the 0th index we subtract one
    return statistic # return solution


def RandomizedQuicksort(A, low, high):
    '''

    :param A: the list which will be sorted
    :param low: the lowest index
    :param high: the highest index
    :return: will return sorted list
    '''
    if low < high: # base case if low = high or is greater then we know we either have one element left or none so we stop
        # otherwise we continue sorting
        pivotIndex = RandomizedPartition(A, low, high) # calls the partition method
        RandomizedQuicksort(A, low, pivotIndex - 1) # recurses over the values less than or equal to pivot to sort
        RandomizedQuicksort(A, pivotIndex + 1, high) #  recurses over the values greatern than to pivot to sort
    return A

def RandomizedPartition(A, low, high):
    '''

    :param A: the list that is being partitioned
    :param low: the low index of the subarray
    :param high: the high index of the subarray
    :return: will call the actual partition method
    '''
    i = random.randint(low, high) # finds a random element from the list
    temp = A[high] # swaps it with the last element to make it the new pivot
    A[high] = A[i]
    A[i] = temp
    return Partition(A, low, high) # calls the partition method with the random element as the pivot

def Partition(A, low, high):
    '''

    :param A: the list that is being partitioned
    :param low: the low index of the subarray
    :param high: the high index of the subarray
    :return: position of the pivot
    '''
    x = A[high] # represents the pivot value
    i = low - 1 # represents the index at which the smaller value subarray ends
    for j in range(low, high): # this will parse through the entire list so that we partition the list into smaller and larger value subarrays
        if A[j] <= x: # if the value is less than the pivot put into the smaller subarray
            i = i + 1 # boundry of smaller subarray increases
            temp = A[j] # swaps the preexisting element with the smaller value found so that the smaller subarray is continous
            A[j] = A[i]
            A[i] = temp
    # the rest of the elements from i+1 to high are the higher elements
    temp = A[i+1] # now place the pivot in the middle of the array
    A[i+1] = A[high]
    A[high] = temp
    return i + 1 # returns the index of the pivot so that we can sort the other subarrays

# Test Drive
A = [2, 5, 1, 16, -4, 2, 6, 9, 11, 7] # tests for duplicates and negative integers
for i in range(1, 11):
    print("The " + str(i) + " statistic is: " + str(statistic(A, i)))
B = []
print("The statistic is: " + str(statistic(B, 1)))
C = [5,2]
print("The statistic is: " + str(statistic(C, 0)))
