'''
Name: Shubham Mohole
Program Description: There are two functions, the first being for the DP version of fibonacci and the second is the coin
exchange program. The DP version of fibonacci will, each time there is a new n, will store the calculated fib(n) into a
dictionary for a quick O(1) lookup the next time it comes up. Fibonacci has repeated subproblems that must be done so
by having a stored n the next time we have to do the fib(n) then we just need to do a lookup. For the coin exchange problem
the main idea is just filling out a grid of dimensions len(elements) x target. The scheme outlined in the responses serves
as the basis for filling out the grid and determining the cell is True or False.
'''


memo = {}
def fibDP(n):
    '''

    :param n: the fibonacci term
    :return: will return the fibonacci value
    '''
    if n < 0:
        return "Invalid Input"
    if n in memo: # if the call is a n-value that we have already found the fibonacci value for we just do a look up of that
        # value
        return memo[n]
    elif n == 0: #if the n value is for fib(0) we already know the fibonacci value to be 0 so this will the base
        # case of our recursion
        return 0
    elif n == 1: # if the n value is for fib(1) we already know the fibonacci value to be 1 so this will the base
        # case of our recursion
        return 1
    else:
        f = fibDP(n-1) + fibDP(n-2) # if n is not 1 or 2 and is a new n value then we will just use the standard fibonacci formula
        memo[n] = f # after we find the value of fib(n) then we want to store it in our dictionary so that if fib(n) comes back
        # up in another recursive call we can just do a lookup
    return f # return the answer


def exactChange(target, coins):
    '''

    :param target: the target sum
    :param coins: the list of coin denominations
    :return: True if target can be reached, False if it cannot
    '''
    if target == 0: # if the target value is 0 then we just do not take any coins so it will always be True no matter the input
        return True
    if len(coins) == 0 or target < 0:
        return False
    rows = len(coins) + 1 # just like in our DP grid in part a) we also want to create grid so that we can which subarray
    # of coins our target can be reached so we have the rows being the elements of our list and the columns being 1...target
    columns = target + 1
    DPGrid = [[False] * columns for i in range(rows)] # default all cells are false
    for i in range(len(DPGrid)): # now we are going to parse through all the cells in the 2-D array
        for j in range(len(DPGrid[i])):
            if i == 0 and j == 0: # we know that if we do not take any elements (which is what the first row represents)
                # then the only true value exists at when our target is also 0.
                DPGrid[0][0] = True
            if i !=0 and j == 0:
                DPGrid[i][j] = False
            if (j == 0): # if the target is 0 then automatically it is True
                DPGrid[i][j] = True
            else:
                if (DPGrid[i-1][j] == True): # now one pattern we find when examining the DP grid was that if a previous
                    # subset of elements added up to a value when we add another element in our subset the previous target is
                    # still a potential sum ( this was the first condition in the scheme that was mentioned)
                    DPGrid[i][j] = True
                else:
                    if (j >= coins[i-1]): # as long as the target is greater than or equal than the row element
                        # NOTE that coins[i-1] is referring to the correct current row element, because i is increased by 1 because
                        # of the first row being the row where we take no elements
                        if (DPGrid[i-1][j-coins[i-1]] == True): # this is the second part of the scheme which is basically if
                            # the target - current row element is True in the row above then this current cell is True
                            DPGrid[i][j] = True
    return DPGrid[rows-1][columns-1] # will return if the the target can be reached

#Test
print("Fibonacci Testing")
print(fibDP(-1))
for i in range(20):
    print(fibDP(i))

print("Coin Exchange Testing")

testList = []
target = 4
print(exactChange(target, testList))
target2 = -9
testList2 = [9, 7, 1, 5]
print(exactChange(target, testList))


coins = [25, 10, 5, 1]
coins2 = [1, 10, 5, 25] # this shows that this works even if the list is not in order
target3 = 6
target4 = 9
print(exactChange(target3, coins))
print(exactChange(target4, coins))

print(exactChange(target3, coins2))
print(exactChange(target4, coins2))

