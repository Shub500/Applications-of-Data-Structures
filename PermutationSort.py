'''
Name: Shubham Mohole
Program: Essentially the program swaps the elements at indices i and j for every index. Afterwards the list is check ed
if it is sorted or not in ascending order and if not the swapping resumes until the list is sorted. To find the average
time it takes for permutation sort based on the length of the array, there is a function called create list which
creates a list of integers from -100 to 100 that is also n long. Then for a hundred test cases that list is sorted
and after each finished sort the time it tooks is added to the total time. Afterwards the total time is divided by the
test cases and we get our average time.
'''



import random # importing important modules to find random integers for the list and indicies
import time

def permutationSort(list):
    '''

    :param list: the list is a list of integers in any order
    :return: will return the sorted list
    '''
    while not sorted(list): # as long as the list is not completely sorted we are going to be swapping elements
        for i in range(len(list)): # the swapping basically works by having by moving index by index and swapping the
            # element at the index with a random index. So the first iteration will have i be 1 then j will equal some
            # random index from i to the end of the list and swap. Then i will become 2, j will be an index between 2 and
            # the end index. This continues until the list is fully parsed. Then the program will check if the list is sorted
            # if not then we do the entire process again
            j = random.randint(i, len(list) - 1)
            temp = list[j]
            list[j] = list[i]
            list[i] = temp
    return list

def sorted(list):
    '''

    :param list: the list is a list of integers in any order
    :return: will return if a list is sorted in ascending order
    '''
    for i in range(len(list) - 1): # checks if every element is sorted by ascending order and if not returns False
        if list[i] > list[i+1]:
            return False
    return True


def benchmarkSort(n,t):
    '''

    :param n: the length of the list that is to be made
    :param t: the number of test cases to be done
    :return: will return the average time it took for a list of length n to be sorted
    '''
    time = 0 # this time variable will be the total time it takes for the array to be sorted testcases times
    for i in range(t):
        L = makeList(n)
        time += timePermutationSort(L) # will add the cumulative times
    avgTime = time / t # then it will find the average by dividing the total time over test case
    return avgTime

# Helper methods:
def makeList(n):
    '''

    :param n: the length of the list that is to be made
    :return: will return a list of integers between -100 and 100.
    '''
    L = []
    for i in range(n):
        L.append(random.randint(-100, 100))
    return L

def timePermutationSort(L):
    '''

    :param L: the list that is going to be sorted
    :return: will return the time it took for permutaionSort to be finished
    '''
    start = time.time() # records the start time
    permutationSort(L)
    end = time.time() # records the end time
    return end - start # the time difference represents the time it took for permuation sort to finish

# Test Drive
for i in range(1, 11):
    print("For array length: " + str(i) + " - Time took: " +  str(benchmarkSort(i, 100)))