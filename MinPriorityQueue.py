'''

Name: Shubham Mohole
A min priority queue is implemented. Four functions have been created: a getter that gets the
size of the heap, Min-Heapify, extract min, and get min which is a getter for the current min in the min queue.
The solution for question 5 is also implemented, though in a different class, it uses a min priority queue
to find the k largest elements.
'''


import math
import random


class MinPriorityQueue:
    def __init__(self, list):
        '''

        :param list: the list of numbers
        '''
        self.minPriorityQueue = list # first
        # we will have our min queue just have the numbers in the default order
        # when we call build heap we will make this queue into an actual min heap
        self.heapSize = len(list)
        # intialize the heap size to be the length of the list because all elements are part of the heap

    def size(self):
        '''

        :return: the current heap size
        '''
        return self.heapSize

    def minHeapify(self, index):
        '''

        :param index: A[i] will float up in the tree to the point where the min heap property is
        A[parent of i] <= A[i]
        :return:
        '''
        l = 2 * index + 1 # we get the index for the left node
        r = 2 * index + 2 # we get the index for the right node
        if l < self.heapSize and self.minPriorityQueue[l] < self.minPriorityQueue[index]:
            # if we have a left node that is in the array and
            # this node has a key value that is smaller than its parent then we set
            # the smallest to the left node because we will want to push it up to the parent position
                smallest = l
        else:
            smallest = index # if not then will then do a comparison of the
            # current key to the right node
        if  r < self.heapSize and self.minPriorityQueue[r] < self.minPriorityQueue[smallest]:
            # this means there is a right node in the heap
                # this means the right node is smaller so we make this the smallest
                smallest = r
        if smallest != index:
            # this means we need to do a swap because we want to push upward the smaller nodes down
            temp = self.minPriorityQueue[index]
            self.minPriorityQueue[index] = self.minPriorityQueue[smallest]
            self.minPriorityQueue[smallest] = temp
            self.minHeapify(smallest) # we then do another recursive call to min heapify so that
            # we keep pushing the smaller node upward in the graph while pushing the larger values down


    def buildMinHeap(self):
        '''

        :return: will return a min priority queue that satisfies the min heap property
        '''
        i = self.size() // 2
        # we start in the middle to ensure that a) the left and right nodes
        # will exist and b) that we can use the property that all the levels below the current i level
        # are min heaps themselves
        while i >= 0:
            self.minHeapify(i)
            i = i - 1
        return self.minPriorityQueue

    def getMin(self):
        '''

        :return: we return the first element in the min priority queue which in a min heap is
        going to be the smallest element
        '''
        return self.minPriorityQueue[0]
        # we do not remove the min just access it

    def extractMin(self):
        '''

        :return: will extract the min, return it, and then min heapify the
        queue to maintain the min heap property
        '''
        if self.heapSize < 1: # input check
            # so that we do not extract something from a non-existing heap
            return "Heap Underflow"
        min = self.minPriorityQueue[0] # we get the min
        # we swap the min and the last element in the heap subarray
        # and we decrease the heap size. This results in two things.
        # First we have removed the min from the heap because now the heap
        # subarray does not include A[i]
        # Second, by swapping we have put as the root of the min heap
        # a value that will be pushed downward and as a result the new min
        # will be pushed up by the min-Heapify call
        self.minPriorityQueue[0] = self.minPriorityQueue[self.size() - 1]
        self.minPriorityQueue[self.size() - 1] = min
        self.heapSize = self.heapSize - 1
        self.minHeapify(0)
        return min

    def insert(self, key):
        '''

        :param key: the value we are adding to the min heap
        :return: will return a min heap with the value and a graph that satisifies the
        min heap property
        '''
        self.heapSize = self.heapSize + 1 # we increase the size of the heap
        # becasue we are adding a new element to the array
        self.minPriorityQueue.append(math.inf)
        # we put a placeholder value which is math.inf because
        # when we update it to inf in the heapIncreaseKey we can push the node up the tree
        self.heapIncreaseKey(self.heapSize-1, key)
        # we call heapIncrease key and we decrease the heap size as a parameter bc of indexing

    def heapIncreaseKey(self, i, key):
        # removed the input restriction of it not being infinite
        # because then when inserting with Q5 the exception got caught
        self.minPriorityQueue[i] = key # we set the placeholder to the actual key
        # we find the parent of this value
        # and begin to swap parent and value until
        # A[parent] < A[i] because then the heap satisifies the min heap property
        parent = i // 2
        while i >= 0 and self.minPriorityQueue[parent] > self.minPriorityQueue[i]:
            temp = self.minPriorityQueue[parent]
            self.minPriorityQueue[parent] = self.minPriorityQueue[i]
            self.minPriorityQueue[i] = temp
            i = parent
            parent = i // 2
random.randint()

class Question5:
    def __init__(self, k, list):
        '''

        :param k: the k largest elements
        :param list: a list of N elements
        '''
        self.k = k
        self.n = len(list)
        self.parentList = list
        self.queue = MinPriorityQueue(self.parentList[0:k])
        # we create a min priority queue object that is
        # filled with the first k elements
        self.queue.buildMinHeap()
        # with those k elements we build a min heap

    def findKLargest(self):
        if self.k == 0: # if k is 0 or less than 0 then we throw an error
            return "Empty"
        if self.k < 0:
            return "Error, input is either 0 or less"
        for i in range(self.k, self.n, 1): # from k+1 to the end of the list with N elements
            # we do a peek of the top of the min heap (which is the smallest element in this priority queue)
            # if the element is bigger then we want to remove and add this new element because
            # we are trying to have our queue store the biggest mins or in essence the maximums
            # we extract the min and then insert the new element using the min heap funcitons
            # so that we maintain min property
            if self.parentList[i] > self.queue.getMin():
                self.queue.extractMin()
                self.queue.insert(self.parentList[i])
        return self.queue.minPriorityQueue # after looping through all N elements we return the min queue




# Tests


test = [10, 9, 8, 7, 6, 5, 4, 3, -1]
testObj = MinPriorityQueue(test)
print("Before insertion " + str(testObj.buildMinHeap()))
testObj.insert(2)
print("After insertion " + str(testObj.buildMinHeap()))
print("Testing min no remove " + str(testObj.getMin()))
print("Tesing min no remove " + str(testObj.minPriorityQueue))
print("Testing min remove: " + str(testObj.extractMin()))
print("Testing min remove " + str(testObj.minPriorityQueue))
print("Size of heap:" + str(testObj.size()))
print("Testing min remove part 2: " + str(testObj.extractMin()))
print("Testing min remove part 2 " + str(testObj.minPriorityQueue))
print("Size of heap:" + str(testObj.size()))
print("--------")
print("Testing Question 5")
testQ5 = [4, 6, 7, 1, 2, 9, 5, 10, 100, 9, 8, 3, 700, 1000]
testObjQ5 = Question5(3, testQ5)
testObjQ5P2 = Question5(5, testQ5)
print(testObjQ5.findKLargest())
print(testObjQ5P2.findKLargest())