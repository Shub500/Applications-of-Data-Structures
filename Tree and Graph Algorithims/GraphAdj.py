'''
Name: Shubham Mohole
Program: The first function is a helper function which takes the .py file with the vertices and edges and creates a
graph using the GraphAdjList module. The second function is main random walks function. Once we have made sure that
the starting vertex is in the graph we get the list of neighbors of the starting vertex. We then randomly select one of
those neighbors to set the current vertex as. We repeat this process knowing that if we do get to a dead end our program
will just go backward since no vertex is isolated completely.
'''



import csv
import GraphAdjList
import random

def createGraphAdjList(file):
    '''

    :param file: the file with all the vertices and connections
    :return: returns a graph
    '''
    graph = GraphAdjList.GraphAdjList() # creates a graph object
    file = open(file, "r")
    valueFile = csv.reader(file, delimiter = "\t") # opens the file and takes values seperated by commas
    edgeList = []
    for x in valueFile:
        for element in x:
            edgeList.append(element.split(",")) # we split the values and then add
    for connection in edgeList: # we check if the vertices are in the graph already and if not then we add the vertex to
        # the dictionary
        if connection[0] not in graph.verticesAdjacencyList.keys():
            graph.addVertex(connection[0])
        if connection[1] not in graph.verticesAdjacencyList.keys():
            graph.addVertex(connection[1])
        graph.addEdge(connection[0], connection[1]) # we then add the connection between the vertices
    return graph


def randomWalk(n, startingVertex, file):
    '''

    :param n: the number of steps being made
    :param startingVertex: the starting vertex from which our walk will begin
    :param file: the file with all the vertices and edges
    :return:
    '''
    graph = createGraphAdjList(file) # calls the above function to create a graph
    currentVertex = startingVertex # we start with the starting vertex
    if currentVertex in graph.verticesAdjacencyList.keys(): # if the vertex is even in the graph we then start walking
        while int(n) > 0:
            adjvertexList = graph.getNeighbors(currentVertex) # we get the list of vertices that are adjacent to our current vertex
            randomIndex = random.randint(0,len(adjvertexList)-1) # we then pick a random index for the random vertex we will
            # walk to
            nextVertex = adjvertexList[randomIndex]
            print("We have walked from vertex " + str(currentVertex) + " to vertex " + str(nextVertex))
            currentVertex = nextVertex # then we set the next vertex to the current vertex and keep walking
            n = n - 1 # we subtract one because we have made a move
        return "Final Vertex is " + str(currentVertex)
    else:
        return "Invalid Vertex"

def TestDrive():
    while True: # as long as the player wants to play the game we will loop to ask for the starting vertex and the
        # the number fo random walks
        game = input("Do you want to play random walk? ")
        if game == "Yes":
            n = input("How many random walks do you want to make? ")
            if int(n) >= 0:
                startingVertex = input("What is the starting vertex? ")
                print(randomWalk(int(n), startingVertex, "GraphAdjSample.py"))
            else:
                print("Invalid Input")
                TestDrive()
        elif game == "No":
            exit(0)
        else:
            print("Invalid Input")
            TestDrive()

TestDrive()

