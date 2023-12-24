'''
Name: Shubham Mohole
Function of Program: For part a) the main idea is that there are two pointers: a start pointer at the low bound and an
    end pointer at the middle point + 1 index. Then the end pointer then moves up 1 until the upper bound is hit so that
    all subarrays with the start index have been searched, then the search pointer is moved up and the proccess repeats
    just before the start index becomes the middle of the array since at all times we want the subarray to be crossing
    the middle

    Finding the max crossing subarray is important because when finding the max subarray three subarrays must be found
    the left hand max subarray, the right hand max subarray, and the crossing max subarray. Then out of those three
    subarray's the max subarray will be found.

    For part b) it is the same logic as in part a) except that same idea as the crossing but the start is the first value
    of the array and then end point increase one by one, then the endpoint will move up by one to get the second index and
    then the third index and so on all the way to the end and then the start point increases going through this entire loop
    again

    For part c) The crossover point was found at n = 3 which makes sense because the BF will be come super inefficient as
    n gets larger since the BF method checks all the possible subarrays while the others recursively do so.

    For part d) As long as the n value is less than 3 then do the the BF method otherwise for n values larger than 3
    do the recursive method
'''

import math, random, time


# Input a list (L) and the low (inclusive) and high (not inclusive) indices for the
# array that you want to find the maximum subarray
# Output will be the left and right indices of the max subarray and the sum
def maxSubarray(L, low, high):
    # if there's only one item in the subarray then the max is it
    if low + 1 == high: return low, high, L[low]

    # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow, leftHigh, leftSum = maxSubarray(L, low, mid)
    rightLow, rightHigh, rightSum = maxSubarray(L, mid, high)

    # check for a max subarray that crosses the midpoint
    crossLow, crossHigh, crossSum = maxCrossingSubarray(L, low, mid, high)

    # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum: return leftLow, leftHigh, leftSum
    elif rightSum >= crossSum:
        return rightLow, rightHigh, rightSum
    return crossLow, crossHigh, crossSum


def maxCrossingSubarray(L, low, mid, high):
    '''
    :param L: The array being looked at
    :param low: the lower bound of the subarray being looked at
    :param mid: the middle of the subarray
    :param high: the higher bound of the subarray being looked at

    No partner
    '''
    # The main idea: have two pointers: a start pointer at the low bound and an end pointer at the middle point + 1 index
    # then the end pointer then moves up 1 until the upper bound is hit so that all subarrays with the start index have
    # been searched, then the search pointer is moved up and the proccess repeats just before the start index becomes
    # the middle of the array.
    startPoint = low  # startpoint is that the farthest left index
    endPoint = mid + 1  # endpoint is currently at the right of the middle index
    upperBound = high  # at the farthest right index
    sumMax = 0  # variable to store the max sum
    finalStartPoint = 0  # to store the subarray pointers that get the maximum sum
    finalEndPoint = 0
    while startPoint < mid:  # as long as the startpoint is less than mid then we can keep moving finding all the subarrays
        # and moving startpoint up
        while endPoint <= upperBound:  # as long as endpoint in within the bounds of the subarray we can keep checking
            # subarrays
            subArray = L[startPoint: endPoint + 1]  # will get the current subarray
            currentSum = sum(subArray)  # will find the sum of the subarray including the endpoint value
            if currentSum > sumMax:  # if the current sum is greater than what is considered max then it will replace max
                # sum
                sumMax = currentSum # the max sum is then stored as well as the indices of the max subarray
                finalStartPoint = startPoint
                finalEndPoint = endPoint
            endPoint = endPoint + 1  # then endpoint will shift up 1

        startPoint = startPoint + 1  # after the internal loop finishes the start point increases

    return finalStartPoint, finalEndPoint, sumMax


def maxSubarrayBF(L):
    '''
    :param L: the list being analyzed
    :return:
    '''
    # Main idea: same idea as the crossing but the start is the first value of the array and then end point increase one by one
    # so 10, then the endpoint will move up by one to get 10 -3 then endpoint move 10 -3 4 all the way to the end then the start point
    # increases going through this entire loop again

    startPoint = 0  # both points will start out on the first index
    endPoint = 0
    sumMax = 0  # create a sum variable to store the max
    finalStartPoint = 0
    finalEndPoint = 0
    while startPoint <= len(L) - 1:
        endPoint = startPoint # set endpoint to startpoint
        while endPoint <= len(L) - 1:
            subArray = L[startPoint: endPoint + 1]
            currentSum = sum(subArray)
            if currentSum > sumMax:
                sumMax = currentSum
                finalStartPoint = startPoint
                finalEndPoint = endPoint
            endPoint = endPoint + 1
        startPoint = startPoint + 1

    # need to find the startPoint and endPoint again because both pointers end at the last index
    return finalStartPoint, finalEndPoint, sumMax


def findDCCrossover():
    n = 3  # the max size of the array in the first test case
    testcases = 5000
    while True:
        dtBF, dtDC = 0, 0  # the dt is the total amount of time each function takes so dtBF is the amount of time the brute
        # force algorithim takes and this may or may not change every test case and the DC is the total recursive algorithim time
        for i in range(testcases):
            L = makeList(n)  # this makes the list of three spaces with random values from -20 to 20
            dtBF += timeBF(L)  # the time after each test is then added to the total for each algorithim
            dtDC += timeDC(L)
        avgBF, avgDC = dtBF / testcases, dtDC / testcases  # then the averages are calculated with the total time over the
        # number of testcases
        if avgDC < avgBF:  # when the recursive algorithim becomes more efficient then it will print out at what size of the array
            # it was efficient at.
            print("DC is faster than BF when n =", n)
            break
        n += 1  # if the BF is still more efficient then the recursive the max array size increase


# Divide and conquer method for solving max subarray that is same as above except
# the base case uses the brute-force strategy when the array is small enough
def maxSubarrayMod(L, low, high):
    ### (d) CHANGE YOUR BASE CASE HERE

    if (len(L) < 3): # the length of the array is less than 3 then BF is faster
        low, high, sum = maxSubarrayBF(L)
        return low, high, sum

        # otherwise, divide the list in half and look for the max subarray in each side
    mid = (low + high) // 2
    leftLow, leftHigh, leftSum = maxSubarray(L, low, mid)
    rightLow, rightHigh, rightSum = maxSubarray(L, mid, high)

        # check for a max subarray that crosses the midpoint
    crossLow, crossHigh, crossSum = maxCrossingSubarray(L, low, mid, high)

        # compare the 3 sums and return the data for the max
    if leftSum >= rightSum:
        if leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
    elif rightSum >= crossSum:
        return rightLow, rightHigh, rightSum
    return crossLow, crossHigh, crossSum


### (d) ENTER THE n WHERE YOUR ORIGINAL DC BECAME FASTER THAN BF
### YOU DO NOT NEED TO COMMENT THIS FUNCTION
def findDCMCrossover():
    testcases = 5000
    count = 0
    print("n\tBF\tDC\tDCM")
    for n in range(1, 11
                   ):  # crossover at 3 3, 2 * 3
        dtBF, dtDC, dtDCM = 0, 0, 0
        for i in range(testcases):
            L = makeList(n)
            dtBF += timeBF(L)
            dtDC += timeDC(L)
            dtDCM += timeDCM(L)
        avgBF, avgDC, avgDCM = dtBF / testcases, dtDC / testcases, dtDCM / testcases
        print(str(n) + "\t" + str(avgBF) + "\t" + str(avgDC) + "\t" + str(avgDCM))

    ### YOU DO NOT NEED TO MODIFY ANY FUNCTION BEYOND HERE BUT IT'S A GOOD IDEA
    ### TO MAKE SURE YOU UNDERSTAND THEM


# returns a list of length n that contains integers in the range -20 to 20

def makeList(n):
    L = []
    for i in range(n):
        L.append(random.randint(-20, 20))
    return L


# returns the time it takes the brute-force method to find the max subarray of L
def timeBF(L):
    start = time.time()
    maxSubarrayBF(L)
    end = time.time()
    return end - start


# returns the time it takes the divide and conquer method to find the max subarray of L
def timeDC(L):
    start = time.time()
    maxSubarray(L, 0, len(L))
    end = time.time()
    return end - start


# returns the time it takes the modified divide and conquer method to find the
# max subarray of L
def timeDCM(L):
    start = time.time()
    maxSubarrayMod(L, 0, len(L))
    end = time.time()
    return end - start


# Test Drive
array = []
print(maxSubarrayBF(array))

array = [5,24,4,-3,6,-9,10,2]
print(maxSubarray(array,2,5))
print(maxSubarrayMod(array, 2,5))
print(maxSubarrayBF(array))

array2 = [-5, -1, 2, 7]
print(maxSubarray(array2,1,3))
print(maxSubarrayMod(array2,1,3))
print(maxSubarrayBF(array2))

findDCCrossover()
findDCMCrossover()
