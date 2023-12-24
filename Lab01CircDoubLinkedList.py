'''
Name: Shubham Mohole
Code Description: Essentially there are two classes CircDoubLinkedList that has Nodes. The Node class has three instance
variables with setter and getter methods for each of them: value, nextNode, prevNode. The linked list will only have a
node head pointer. If the inserted node is the first one that makes it the head, if not then the inserted node will become
the new head with the old head's pointers. To search the entire linked list is iterated through for the same value. A key
assumption is that all values added are unique. To delete a node we first search for that node's pointer and then remove it,
then reconfiger the pointers.

'''


class Node:
    def __init__(self, value):
        '''

        :param value: Value of the node is just the item it is holding.
        Also then the next and previous nodes are set to a default None
        '''
        self.value = value
        self.nextNode = None
        self.prevNode = None

    def setNextNode(self, nextNode):
        '''

        :param nextNode: The new next node will be set as the next node of the Node instance
        :return:
        '''
        self.nextNode = nextNode

    def setPrevNode(self, prevNode):
        '''

        :param prevNode: The new previous node will be set as the previous node of the Node instance
        :return:
        '''
        self.prevNode = prevNode

    def getNextNode(self):
        '''

        :return: will return the next node
        '''
        return self.nextNode

    def getPrevNode(self):
        '''

        :return: will return the previous node
        '''
        return self.prevNode

    def getValue(self):
        '''

        :return: will return the vaue of the node
        '''
        return self.value


class CircDoubLinkedList():
    def __init__(self):
        '''
        The headNode is set to be None for now because there is no head
        '''
        self.headNode = None

    def getFirst(self):
        '''

        :return: will return the headNode index
        '''
        return self.headNode

    def insert(self, item):
        '''

        :param item: The new item inserted will be inserted into the linked list
        :return: There will be no return statements
        '''
        if self.headNode == None: # if this is the first node inserted then head will be none after execution then
            # the head node will be created
            self.newNode = Node(item)
            self.headNode = self.newNode
            self.newNode.setNextNode(self.newNode)
            self.newNode.setPrevNode(self.newNode)
        else: # if already there is a head node then the new node constructed will have two pointers going to the head
            # and a pointer to the current tail
            self.newNode = Node(item) # a new node is created
            tailofCurrentHead = self.headNode.getPrevNode() # the tail node is stored before being lost
            self.newNode.setNextNode(self.headNode) # the new node gets connected to the old head
            self.newNode.setPrevNode(tailofCurrentHead) # the new node gets connected to the tail
            self.headNode.setPrevNode(self.newNode) # the old head gets connected with the new node (head)
            tailofCurrentHead.setNextNode(self.newNode) # the tail gets connected with the new node (head)


    def search(self, item):
        '''

        :param item: The list will be search through for the item until the the list has been looped
        :return: The function will return if the value was found or not found
        '''
        if self.headNode.getValue() == item: # if the item is the head then return the head
            print("Value was found")
            return self.headNode
        else: # if not then iteration begins
            currentNode = self.headNode.getNextNode() # since the head was already check we will start on the next node
            looped = False # the looped variable will keep track of if we looped the list
            while not looped:
                if currentNode == self.headNode: # looped will become true if the current node has reaced the head node
                    looped = True
                    print("Linked List was looped and could not find item")
                    return None
                else:
                    if currentNode.getValue() == item: # check if the value of the node is equal to the item
                        print("Value was found")
                        return currentNode
                    else:
                        currentNode = currentNode.getNextNode() # if the current node is not the item we will look at
                        # the next node

    def delete(self, item):
        '''

        :param item: If the item is found then the entire list is iterated through to check for the item and then the node
        carrying the item will be removed
        :return: It will return either that the item was not found or nothing indicating that the removal was succesful
        '''
        nodeToRemove = self.search(item)
        if nodeToRemove == None:
            print("Node that was asked to be removed does not exist")
            return None
        else:
            if(nodeToRemove == self.headNode):
                    self.headNode = nodeToRemove.getNextNode()
            nodeToRemove.getPrevNode().setNextNode(nodeToRemove.getNextNode()) # will set the previous node's next
            # connection to the removed node's next connection
            nodeToRemove.getNextNode().setPrevNode(nodeToRemove.getPrevNode()) # will set the next node's
            #  previous conection to the removed node's previous connection

            nodeToRemove.setPrevNode(None) # both connections from B are broken
            nodeToRemove.setNextNode(None)


    def __str__(self):
        '''

        :return: will print out each node until the list has been looped
        '''
        currentNode = self.headNode # will print each node
        while currentNode:
            print(currentNode.getValue())
            currentNode = currentNode.getNextNode()
            if(currentNode == self.headNode):
                exit(1)

list = CircDoubLinkedList()
list.insert("A")
list.insert("B")
list.insert("C")
list.search("B")
list.search("uyurh")
list.delete("C") # the delete functions call search so that is why you will see things like "Value was found" or "Linked
# List was looped and could not find item"
list.insert("D")
list.insert("E")
list.delete("C")
list.__str__()
