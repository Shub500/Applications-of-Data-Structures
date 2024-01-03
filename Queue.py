'''
Name: Shubham Mohole
Code Description: The Queue is created with two stacks. Each stack will have a top pointer.
The first stack is queue stack where the elements are pushed in which simulates enqueue. The second stack will be the
queue that dequeues the element. The basic functionality is that when a dequeue occurs all of the elements in the
queue stack goes into the pop stack in reverse order so that the top of pop stack will be the element that will be
dequeued. Then the values of pop stack are transferred back into pop stack so that the order of the queue is kept. '''

class Queue:
    def __init__(self, n):
        '''

        :param n: maximum size of the array

        This function creates two stacks of n length and head pointers to the beginning of the stacks
        '''
        self.arrSize = n
        self.queueStack = [None] * n
        self.top1 = -1
        self.popStack = [None] * n
        self.top2 = -1

    def length(self):
        '''
        :return: will return the length of the stack by adding one to the top the queue stack because at all times
        the queue stack will hold the elements
        '''
        return self.top1 + 1

    def push(self, stackNum, item):
        '''
        The top pointer moves up and the item gets added to the top of the stack
        :param stackNum: gets the stack number so 1 is for queue stack and 2 is pop stack
        :param item: the item being added
        :return: It will not return anything except if there is an issue like for example the stacks are empty meaning
        there is no space for a element to be added...Note that this is different from having a stack with just None values
        since that kind of stack still has a length.
        '''
        if item == None: # if the item nothing then None will be returned
            return None
        elif stackNum == 1:
            if len(self.queueStack) != 0:# if the push is happening at the stack 1 then:
                self.top1 = self.top1 + 1  # moves the head pointer up and inserts the item
                self.queueStack[self.top1] = item
            else:
                print("Queue Stack is empty")
                return None
        elif stackNum == 2:
            if len(self.popStack) != 0:
                self.top2 = self.top2 + 1
                self.popStack[self.top2] = item
            else:
                print("Pop Stack is empty")
        else:
            print("Invalid Stack Number")
            return None
            # if the stack number is not 1 or 2 then it is invalid

    def pop(self, stackNum):
        '''
        :param stackNum:  gets the stack number so 1 is for queue stack and 2 is pop stack
        :return: it will return the popped value
        '''
        if stackNum == 1:
            transferValue = self.queueStack[self.top1]  # stores the value on the top of StackQueue
            self.queueStack[self.top1] = None  # changes that index to None
            self.top1 = self.top1 - 1  # moves the top pointer down one to the next non-None value
            return transferValue
        elif stackNum == 2:
            poppedValue = self.popStack[self.top2]  # stores the value on the top of PopQueue
            self.popStack[self.top2] = None  # changes it to None
            self.top2 = self.top2 - 1  # moves the top pointer down one to the next non-None value
            return poppedValue
        else:
            print("Invalid Stack Number")
            return None


    def enqueue(self, item):
        '''

        :param item: the item that is being pushed
        :return: will call the push function to be processed
        '''
        self.push(1, item)

    def dequeue(self):
        '''
        # Scenarios: A) StackQueue has elements and PopStack has none so then transfer of elements occurs and pops the
        top of PopStack

        B) PopStack has an element

        C) StackQueue does not have an element and Pop Stack does not have an element
        :return: It will return the popped element

        '''
        if self.top1 != -1:
                while self.queueStack[self.top1] != None:  # this condition would represent that all the values in
                    # StackQueue are None
                    self.push(2, self.pop(1))  # the second parameter calls the pop function which will return the
                    # popped
                # value while keeping the array size of the stacks the same
                poppedValue = self.pop(2)  # will return the top of stack 2
                while self.popStack[self.top2] != None:
                    # then all the values are going to transferred back to queue stack
                    self.push(1, self.pop(2))
                return poppedValue
        else:
            print("No values in queue")
            return None # if no values in queue stack then there are no elements


    def TestDrive(self):
        self.dequeue()
        self.enqueue("A")
        self.enqueue("B")
        self.enqueue("C")
        self.enqueue("D")
        print(self.length())
        self.dequeue()
        self.dequeue()
        self.enqueue("E")
        self.dequeue()
        self.dequeue()
        self.enqueue("F")
        self.dequeue()
        self.dequeue()
        self.enqueue("G")
        print("Queue Stack:")
        print(self.queueStack)
        print("Pop Stack:")
        print(self.popStack)


test = Queue(5)
test.TestDrive()


