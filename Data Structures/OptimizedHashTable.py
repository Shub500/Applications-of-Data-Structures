'''
Name: Shubham Mohole
Code Description: All the functions in the lab are part of the class StudentHashTable, because I thought it would be easier
just in terms of organization and testing. The constructor of the class is to initialize a bucket array that has
length depending on what the user wants the length to be. The functions are split into two categories the Unicode
verison and the Python version. The real difference between the two is how the hash value is calculated since the unicode
version sums the value each letter has the mods by the bucket size while the Python hash uses the hash() function and
then mods by the bucket size. First, we add all the students from tsv file into the hash table. When we find the index to
put the element, we first check if that bucket is empty or not. If it is empty then we just add the student. If not
we know we are going to have a collision, so our collision counter goes up and we add the name to that subarray. Lastly we have
a lenght function that just finds the length of the array in each  bucket which is the number of keys added.
'''



import csv # to read the tsv file

class StudentHashTable(object):
    def __init__(self, length):
        '''

        :param length: the length of the buckets being used
        '''
        self.length = length
        self.array = [None] * length
        self.collisionCounter = 0 # a total collision counter
    def calculateHash(self, key, numBuckets):
        '''
        :param key: the key is a string
        :param numBuckets: the number of buckets in the hash table
        :return: the result of modding the sum of the Unicode values for every letter of the key by the number of buckets
        '''
        sumOfValues = 0 # will store the sum of the unicode values
        for i in range(len(key)): # will loop through each letter of the string
            sumOfValues = sumOfValues + ord(key[i]) # will find the unicode equivalent of the letter then add it
        return sumOfValues % numBuckets # modules the sum and the number of buckets which will get us the index to input
    # the value in

    def calculatePythonHash(self, key, numBuckets):
        '''

        :param key: the key is a string
        :param numBuckets: the number of buckets in the hash table
        :return: the result of using python's hash function modded by the number of buckets
        '''
        return hash(key) % numBuckets

    def addStudentUnicode(self, key, value):
        '''

        :param key: the name of the student
        :param value: the grade the student is in
        :return: will have added all names and grades into the hash table
        '''
        index = self.calculateHash(key, len(self.array)) # will get the index for which the value is inserted into
        if self.array[index] is None: # if there is no element then we need to create a list in that index
            self.array[index] = [] # creates a list at that index
            self.array[index].append( [key, value] ) # then we will just add the key value pair to the list
        else:
            # now we be adding a new key value pair to this
            # array but we have a collision
            self.collisionCounter = self.collisionCounter + 1
            self.array[index].append([key, value])

    def addStudentPython(self, key, value):
        '''

        :param key: the name of the student
        :param value: the grade the student is in
        :return: will have added all names and grades into the hash table
        '''
        index = self.calculatePythonHash(key, len(self.array)) # will get the index for which the value is inserted into
        if self.array[index] is None: # if there is no element then we need to create a list in that index
            self.array[index] = [] # creates a list at that index
            self.array[index].append( [key, value] ) # then we will just add the key value pair to the list
        else:
            # now we be adding a new key value pair to this
        # array but we have a collision
            self.collisionCounter = self.collisionCounter + 1
            self.array[index].append([key, value])

    def findStudentsUnicode(self):
        '''

        :return: returns the students that have the same name hash value as me in the unicode version
        '''

        # to find the names that have the same index we can first just insert all the students
        # into the hash table and then we would just parse through the list where my name is located at, printing all the other names
        index = self.calculateHash("Mohole, Shubham", self.length)
        for element in self.array[index]:
            print(element[0], element[1], str(self.calculateHash(element[0], self.length))) # will print out name-grade-hash value for each student

    def findStudentsPython(self):
        '''

        :return: returns the students that have the same name hash value as me in the unicode version
        '''
        # to find the names that have the same index we can first just insert all the students
        # into the hash table and then we would just parse through the list where my name is located at, printing all the other names
        index = self.calculatePythonHash("Mohole, Shubham", self.length)
        for element in self.array[index]:
            print(element[0], element[1], str(self.calculatePythonHash(element[0], self.length))) # will print out name-grade-hash value for each student

    def lengthAtEachIndex(self):
        '''

        :return: the length of the subarray in the bucket
        '''
        for i in range(len(self.array)):
            if self.array[i] == None: # if the array is empty then there were no keys mapped
                print("The length of the array at index " + str(i) +" was 0")
            else:
                length = len(self.array[i]) # otherwise find the length which will correspond to the number of keys
                print("The length of the array at index " + str(i) +" was " + str(length))


    def getCollisionCounter(self, bucketSize):
        '''
        :return: returns the total number of collisions
        '''
        return self.collisionCounter

# Test
file = open('/Users/shub/Desktop/Lab05Data.tsv')
tsvreader = csv.reader(file, delimiter = "\t")
header = next(tsvreader)
print(header)
print("-----Unicode Hash------")
Students = StudentHashTable(100)
for element in tsvreader:
    Students.addStudentUnicode(element[0], element[1])

print(Students.array)
print("--------")
Students.findStudentsUnicode()
print("--------")
Students.lengthAtEachIndex()
print("The number of collisions: " + str(Students.getCollisionCounter(100)))
file.close()




print("-----Python Hash-----")
fileII = open('/Users/shub/Desktop/Lab05Data.tsv')
tsvreaderII = csv.reader(fileII, delimiter = "\t")
StudentsII = StudentHashTable(100)
for elementII in tsvreaderII:
    StudentsII.addStudentPython(elementII[0], elementII[1])

print("--------")
print(StudentsII.array)
print("--------")
StudentsII.findStudentsPython()
print("--------")
StudentsII.lengthAtEachIndex()
print("--------")
print("The number of collisions: " + str(StudentsII.getCollisionCounter(100)))



