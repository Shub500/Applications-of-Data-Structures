'''
Name: Shubham Mohole
Code Description: I create an array of 3n that will hold n values and for each value there is going to a previous and next
pointer which will be adjacent indices: For example i will hold the value, i+1 will be the next value pointer, and i+2
will be the previous value pointer. There are two "sub lists" that are also maintained with the free linked list and the
value linked list. In hindsight, to add an item in the value linked list, first a free node is captured and then its value
slot will be the item that is being inserted and then its next pointer will be None since we are adding to the tail of
the value list and the previous pointer will be the previous tail. To delete, the pointers are changed to continue the
linked list and then a free node is added to the free node list.

'''


class DLLArray:
    def __init__(self, n):
        '''

        :param n: N represents how many items will be stored and because each item will need in its "node" a previous
        and next index the list will be 3n
        '''
        self.maxListSize = n
        self.storageArray = [None] * (3 * self.maxListSize) # the list is going to be three times as large
        # than the number items it will hold because I need to store the previous and next node
        self.headOfFreeList = 0 # will be a pointer to the current head of the free list
        currentIndex = 0
        while(currentIndex <= len(self.storageArray) - 6): # this loop will create the freeList which will have
            # stored the index to the next free node: ex. at index 0 value 3 will be placed and that value is pointing
            # to index 3 which is free node and index 3 has a value of 6 pointing to the next index marking a free node
            self.storageArray[currentIndex] = currentIndex + 3
            currentIndex = currentIndex + 3
        self.headOfValueList = None # will be a pointer to the current head of the value list

    def allocate(self):
        '''

        :return: will return the head of the free node list and if there is none that means the array is full
        '''
        if self.headOfFreeList != None: # so if there is a free list then the head of that free list will be saved and
            # the new head will be the next free node which is easy to find because the value that the current head is
            # holding is pointing to the index with a free node
            savedFreeListHeader = self.headOfFreeList
            self.headOfFreeList = self.storageArray[savedFreeListHeader]
            return savedFreeListHeader
        else:
            # then there are no free nodes signifying that the list is full of value
            print("Array is full")
            return None

    def freeNode(self, index):
        '''
         In the storage array each node array occupies p, p+1, p+2 [assuming value of the node can be stored in one array
         element]. In this method, given the index in the array
        we are calculating the index p as the starting location of the node storage and returning whether that storage
         free or not
        :param index: The index that is sent should be an index pointing to a value of a node
        :return: The return will either be that the index was invalid or that there it is not a free node or that the
        node is free
        '''
        if (index < 0 or index > len(self.storageArray) or index%3 != 0): # check if the index even inputted is valid
            return "Invalid index inputted"
        if (self.headOfValueList == index):
            return "It is not a free node"
        if (self.storageArray[index + 1] == None and self.storageArray[index + 2] == None): # checks
            # if the next two values are None because that reprsents a free node ( free nodes only have a value correspoding
            # to the next free node
            return "It is a free node"
        else:
            return "It is not a free node"

    def insert(self, item):
        '''

        :param item: The item will be added to the value list if there is space in the array
        :return: The return will only happen if there is an error meaning that there is no free node
        '''
        newNodeIndex = self.allocate() # we will get a free node's index and store it
        if (newNodeIndex == None): # if that index is 0 then we know the list if full
            return "List is Full"
        self.storageArray[newNodeIndex] = item # if not then the first index of the "node" will have the value
        self.storageArray[newNodeIndex + 1] = None # then the second index of the "node" will have a pointer of None
        # because the insertion is happening will be the tail of the value list so there is no next

        if (self.headOfValueList == None): # if the head is empty then the new "node" will be at the head
            self.headOfValueList = newNodeIndex
        else:
            nextPrevNotSet = True # else then we will have to adjust the pointers so that previous pointer of the
            # tail node so we iterate through the value list in search for a "node" that has None has its next pointer
            # and then we connect with the new Node
            currentIndex = self.headOfValueList
            while(nextPrevNotSet == True):
                if (self.storageArray[currentIndex + 1] == None):
                    self.storageArray[currentIndex + 1] = newNodeIndex
                    self.storageArray[newNodeIndex + 2] = currentIndex
                    nextPrevNotSet = False
                else:
                    currentIndex = self.storageArray[currentIndex + 1]

    def search(self, item):
        '''

        :param item: Will search the entire value linked list for the item
        :return:  Will return the index when the item is found or None
        '''
        currentIndex = self.headOfValueList # the search is very simple since all we are doing is starting at the
        # head of the value list and then going through each "node" checking if the value of the "node" is equivalent
        # and then returning the index
        if (currentIndex == None):
            return None
        while(currentIndex != None):
            if (self.storageArray[currentIndex] == item):
                return currentIndex
            else:
                currentIndex = self.storageArray[currentIndex + 1]
        return None

    def delete(self, item):
        '''

        :param item: Will delete the item by parsing through the list and getting the "node" that has the value and then
        reconfigering the adjacent node's pointers
        :return: will return None if the item is not found
        '''
        indexToDeleteItem = self.search(item) # first we find the index of the item we are going to delete
        if (indexToDeleteItem == None): # a check for validity
            return None

        nextIndex = self.storageArray[indexToDeleteItem + 1] # now we are going to store what the soon-to-be deleted
        # node's previous and next indices are
        prevIndex = self.storageArray[indexToDeleteItem + 2]
        self.storageArray[indexToDeleteItem + 1] = None # we then start to make this node a free node by cancelling out
        # the "node's" pointer
        self.storageArray[indexToDeleteItem + 2] = None

        if (self.headOfValueList == indexToDeleteItem): # if the node to remove is the head then we make the new head
            # of the value list be the next index of the soon to be deleted head
            self.headOfValueList = nextIndex

        if(nextIndex != None): #
            self.storageArray[nextIndex + 2] = prevIndex # the next "nodes" previous index needs to be changed to be the
            # soon-to-be removed node's previous node
        if (prevIndex != None): #
            self.storageArray[prevIndex + 1] = nextIndex # the previous "nodes" next index needs to be changed to be the
            # soon-to-be removed node's next node

        self.storageArray[indexToDeleteItem] = self.headOfFreeList
        self.headOfFreeList = indexToDeleteItem

    def __str__(self):
        '''

        :return: will print out the array and also after every "node" it will partition it in the string
        '''
        for element in self.storageArray:
            print(str(element), end=" ") # the end will give space to each element


        #print()
        #if (self.headOfValueList != None):
        #    print("Head of Value List: " + self.backupStr(self.headOfValueList))
        #if (self.headOfFreeList != None):
            print("Head of Free List: " + self.backupStr(self.headOfFreeList))

    def backupStr(self, string):
        '''
        :return: the original string was not printing the search values so this prints the search value
        '''
        if (string == None):
            return "None"
        return str(string)

    def TestDrive(self):
        self.delete("A") # to check if I delete in empty list
        print(self.__str__())

        print(self.__str__())
        self.insert("A")
        print(self.__str__())
        self.insert("B")
        print(self.__str__())
        self.insert("C")
        print(self.__str__())
        self.insert("D")
        print(self.__str__())
        self.insert("E")
        print(self.__str__())

        print("Search List " + self.backupStr(self.search("A")))
        print("Search List " + self.backupStr(self.search("B")))
        print("Search List " + self.backupStr(self.search("C")))
        print("Search List " + self.backupStr(self.search("D")))
        print("Search List " + self.backupStr(self.search("E")))

        self.delete("B")
        print(self.__str__())

        self.delete("A")
        print(self.__str__())

        self.delete("C")
        print(self.__str__())

        self.delete("D")
        print(self.__str__())

        self.delete("E")
        print(self.__str__())

        self.insert("F")
        print(self.__str__())

        self.insert("G")
        print(self.__str__())

        print(self.freeNode(3))
        print(self.freeNode(2))
















