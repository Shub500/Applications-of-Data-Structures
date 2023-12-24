'''
 Name: Shubham Mohole
 Code Description: The code below implements two stacks in one array of length n.
 Essentially to utilize all of the array space and not to create overflow I had one stack start at the very beginning
 of the stack and the other starting at the very end. Then when items are added, depending on the stack, the item will
 be added going to the right or to the left (adding items will occur in opposite directions).
 Overflow is detected if the top of the stack #1 + 1 is equal to the top of the stack #2
'''

class TwoStacks:
    def __init__(self, n):
        '''

        :param n: The maximum size of the array
        '''
        self.arr = [None] * n  # This creates an array of length n of None values
        self.arrSize = n
        self.head1 = -1  # this sets the head of stack 1 is at position -1 because
        # when the first element is added in position 0 then the head1 will be updated correctly to be
        # at position 0
        self.head2 = n  # this sets the head of stack 2 at n because similar to head 1 when the first item in stack2
        # is added then the head2 will move into the correct position of n-1

    def height(self, stackNum):
        '''

        :param stackNum: The stack number corresponds to the stack
        :return: It will return the height of the stack
        '''
        if stackNum == 1:
            return self.head1 + 1 # to find the length just found the position of h1 and added 1 because the list
            # starts at 0
        elif stackNum == 2:
            return self.arrSize - self.head2  # to find the length just subtracted the array size from the postion of
            # second stack
        else:
            print( "Invalid stack number inputted")
            return None

    def push(self, stackNum, item):
        '''

        :param stackNum: The stack number corresponds to the stack
        :param item: The item is the item being added
        :return: It will return an error message if there is a problems otherwise there will not be a return of the
        modified array
        '''
        if stackNum == 1:  # condition to check which stack is being modified
            if not self.head1 + 1 == self.head2:  # this checks for stack overflow since if the next head is at the
                # head of stack 2 then there is no more space in the array
                self.head1 = self.head1 + 1  # if condition is passed then head moves up
                self.arr[self.head1] = item  # and the item is inserted as well
            else:
                print("Stack 1 Overflow")
                return None  # if the previous condition fails an error message pops up
        elif stackNum == 2:
            if not self.head1 == self.head2 - 1:
                self.head2 = self.head2 - 1  # if condition is passed then h2 moves down
                self.arr[self.head2] = item
            else:
                print("Stack 2 Overflow")
                return None
        else:
            print("Invalid stack number inputted")
            return None

    def pop(self, stackNum):
        '''
        :param stackNum: The stack number corresponds to the stack
        :return: Will return the popped value
        '''
        if stackNum == 1:
            if self.head1 >= 0: # this conditions check if a item is even in the list.
                # Because I started at -1 for the position of h1 if no items were added in the stack then h1 would be at
                # -1 and there would no reason to remove any element hence h1 needs to be greater than or equal to 0
                poppedValue = self.arr[self.head1]
                self.arr[self.head1] = None
                 # because stacks are last one in first one out whatever the last item
                # added was it is going to be where the head of the stack is so taking out the head of the stack is
                # removing the element
                self.head1 = self.head1 - 1 # head gets shifted left
                return poppedValue
            else:
                print("No items in Stack 1")
                return None
        elif stackNum == 2:
            if self.head2 < self.arrSize: # as long as head2 and arrSize are not equal or greater then that means there
                # are values in stack2
                poppedValue = self.arr[self.head2] # value is stored is going to get popped
                self.arr[self.head2] = None
                self.head2 = self.head2 + 1 # then the head will increase since the previous value at the index was
                # "deleted"
                return poppedValue
            else:
                print("No items in Stack 2")
                return None
        else:
            print("Invalid Stack Number")
            return None



    def __str__(self):
        '''

        :return: prints the array
        '''
        print(self.arr) # prints the array

    def TestDrive(self):
        self.pop(1)
        self.push(2,10)
        self.push(2,15)
        self.push(1,11)
        self.push(1,45)
        self.push(1, 85)
        self.push(2, 89)
        self.push(2, 39)
        self.push(2, 78)
        self.push(2, 40)
        self.push(2,66)
        self.push(2,45)
        self.__str__()
        print("Popped element from stack1 is " + str(test.pop(1)))
        print("Popped element from stack2 is " + str(test.pop(2)))
        print(self.height(1))
        print(self.height(2))
        self.__str__()


test = TwoStacks(10)
test.TestDrive()

