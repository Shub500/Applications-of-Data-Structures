
# simple reverse list

def reverse(list):
    if list <= 1:
        return list
    return list[1:len(list)] + list[0]

class LinkedListNode:
    def __init__(self,value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self,newNext):
        self.next = newNext





def insert(self, value):
    node = LinkedListNode(value)
    if self.head == None:
        self.head = node
    else:
        node.setNext(self.head)


# delete kth
# Main Idea: look at the first node then subtract by k then look at the next node until k becomes 1 then remove the node
def delete(currentNode, k):

    if k == 1:
        list.remove(currentNode)

    else:
        nextNode = currentNode.getNextNode()
        newNode = delete(nextNode, k - 1)


# reverse single linked list

# def reverse(self, currentNode = self.headNode):
#     if (currentNode == None or currentNode.nextNode == None):
#         return currentNode
#     nextNode = reverse(currentNode.nextNode)
#     currentNode.getnextNode.setnextNode(currentNode)
#     currentNode.nextNode = None
#     return nextNode

# reverse from m to n

def reverseFirstN(head, n, nextNode = None):
    if n==1:
        nextNode = head.nextNode
        return head
    lastNode = reverseFirstN(head.nextNode, n-1, nextNode)
    head.nextNode.nextNode = head
    # head.nextNode = successor
    return lastNode

def reverseBetween(head, m, n):
    if m == 1:
        return reverseFirstN(head, n)
    head.nextNode = reverseBetween(head.nextNode, m -1, n-1)
    return head



# reverse double linked list
def reverse(node):
    if not node: # if there are no node in the list then return None
        return None

   # swap the pointers for the node
    temp = node.getNextNode()
    node.setNextNode(node.getPrevNode)
    node.setPrevNode(temp)

    if not node.getPrevNode(): # that means that the previous node does not exist meaning that the head was just reversed
        # so that means that the list has been reveresed
        return node

    return reverse(node.getPrevNode) # keep going if head not reached

# to delete entire linked list
def deleteList(head):
    if head == None: # reached tail
        return
    deleteList(head.getNextNode())


# print alternate nodes

def printAlternate(node, isOdd):
    if node == None:
        return
    if (isOdd == True):
        print(node.getValue)
        isOdd = False
    else:
        isOdd = True
    printAlternate(node.getNextNode(), isOdd)

# check if linked list is palindrome

# def isPalindrome(headNode):
#     front_pointer = headNode
#
#     def recursive_check(current_node = headNode):
#         if current_node is not None:
#             if not recursive_check(current_node.getNextNode()): # if the next node's recursive call is False then break
#                 # right now
#                 return False
#             if front_pointer.getValue != current_nod.getValue(): # if the first and last elements are not equal then
#                 # break right now
#                 return False
#             front_pointer = front_pointer.getNextNode()
#         return True
#
#     return recursive_check()


# intersection node from two linked lists
# basically get the larger linked list pointer to the same index as the head of the smaller head index
sum = 0
lim = 20
current = 1
