'''
Name: Shubham Mohole
Program: Below is the recursion menu. I found it easier to understand if I wrote code description in the functions itself
so please refer to each function for an explanation on how it works. In many cases, I have to float the input which is neccesary
because when the user inputs a number or array it actually comes as a string.
'''
def palindrome(string):
    '''

    :param string: the word being entered
    :return: True or false if the word is a palindrome
    '''
    if len(string) <=1: # we know that if the string length is just one letter automatically that is a palindrome
        return True
    elif string[0] == string[len(string) - 1]: # if the first and last letter of the word are the same then we may
        # have a palindrome so we are now going to substring the main string by checking if the letters are symetrical
        return palindrome(string[1: len(string) - 1]) # so now all we do go in by one so lets say "racecar" was our example
        # then since the first and last letters are equal we go in by one so we check the first index and the second to
        # last index then we check the third index and the third to last index and so on
    else:
        return False


def digitsToWords(n):
    '''

    :param n: is a string number that comes in but then is converted into a float
    :return: return's the word to digit
    '''

    # The main idea: Lets say we have the number 457. Now 457 does not have a decimal,
    # so now the call digitsToWords(45.7) is made with "seven" being returned because we moduled by 10. Now you might be
    # wondering why decimals are being used, well it is a convenient form of keeping track of what digits we have covered
    # and what other digits need to be translated. Going back to the exmaple now 45.7 is the n. Of course it has a decimal
    # so then we call digitsToWords(4.57) and return the integer of 45.7 which is 45 and module by 10 which gets us "five".
    # We do the same thing with 4.57 where we return "four" and call digitsToWords(0.457). Now the base case gets hit
    # because the the integer version of 0.457 is 0 meaning we are done

    n = float(n)
    numToWordDict = {0: "zero ", 1: "one ", 2: "two ", 3: "three ", 4: "four ", 5: "five ", 6: "six ", 7: "seven ",
                     8: "eight ", 9: "nine "} # dictionary that holds the number to string values
    if int(n) == 0: # essentially if the number is less than 0 then that stops the recursion
        return ""
    if int(n) != n: # decimal case since the integer of a decimal is not equal to the original value because values are
        # truncated
        return digitsToWords(n/10) + numToWordDict[int(n) % 10]
    else: # no decimal case (refer above for the logic behind the decimal case)
        return digitsToWords(n/10) + numToWordDict[n % 10]

def sumToTarget(nums, x):
    '''

    :param nums: list of positive integers
    :param x: the target
    :return: returns either true or false if there is a subset that sums to x
    '''

# Note this function functions with positive integers, however to tackle a list of both positive and negative integers
    # then a way to solve the problem is to test all permutations of subsets and then check if any of the sums equals the
    # the target sum however that will be a very inefficient because of instead of limiting the length of the list as
    # this function does.
    if x == 0:
        return True
    if len(nums) == 0: # this basically says that if the length of the list is 0 then the list has been parsed and
        # there are no subsets that provide the target sum
        return False
    if (nums[len(nums) - 1] > x): # logically if the last element of the list it cannot fit in any subset because if all the
        # integers are positive than they cannot sum to the target for example if the target was 7 and the last element
        # is 10 then 10 can be removed because 10 will not be in any subset
        return sumToTarget(nums[0: len(nums) - 1], x) # there are two options with the list just shrinking from the right because
        # the last index is bigger than the subset
    else:
        return sumToTarget(nums[0: len(nums) - 1], x - nums[len(nums) - 1]) # if the highest element is less than the target
    # all we have to do now is to find a subset that x - the highest element. For example if the target was 7 and 4 was the
    # last element then all we have to look for in the shrinked array a sum of 3.


def choose(n, k):
    n = float(n)
    k = float(k)
    if k == 0: # for example if we have 5 choose 0 even though we are not choosing any of the five items we will still
        # have that original set of the five items making it 1 combination
        return 1
    elif k > n: # if k becomes bigger we know that does not make sense because for 5 choose 6 one cannot select 6 items
        # from an set of only 5 items
        return 0
    else:
        return choose(n-1, k) + choose(n-1, k-1) # the recursive formula

def RecursionMenu():
    while True:
        print("Welcome to the Recursion Calculator")
        decision = int(input("Choose a function:" + "\n" + "1) Palindrome" + "\n" + "2) digitsToWords" + "\n" + "3) sumToTarget"
                    + "\n" + "4) choose"
                    + "\n" + "5) quit"))

        if decision == 1:
            word = str(input("Please enter a word"))
            print(palindrome(word))

        elif decision == 2:
            integer = int(input("Please enter an integer"))
            if integer == 0:
                print("zero") # if the input is 0 then it should return 0
            else:
                if integer < 0: # this accounts for the number is negative a negative sign is just place in front
                    integer = float(integer)
                    integer = integer * -1
                    print("-" + digitsToWords(integer))
                else:
                    print(digitsToWords(integer))

        elif decision == 3: # need to get a list of elements for the sumToTarget
            nums = []
            length = int(input("Please enter size of list: "))
            for i in range(length):
                item = int(input("Element: "))
                if item >= 0:
                    nums.append(item)
                else:
                    print("Element added was negative")
                    exit(1)
            x = int(input("Please enter an integer: "))
            print(sumToTarget(nums, x))

        elif decision == 4:
            n = int(input("Please enter an integer"))
            k = int(input("Please enter another integer"))
            print(choose(n, k))

        elif decision == 5:
            exit(1)
            break

        else:
            print("Invalid input")

# Test Drive
