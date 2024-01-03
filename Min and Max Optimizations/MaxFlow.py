'''
Name: Shubham Mohole
Program Description: Our program has three classes: a Node class, an Edge Class, and a Network class all with
the specified instance variables as well as some lists and dictionaries that help in organizing the network's edges
and vertices. We also include one helper method called getEdge which gets the edge between (u,v) or if there is none
returns None. The two main functions find_residual and solve_network are modelled after the Ford-Fulkerson method.
The find_residual finds an augmenting path through edges that will reach from S to T. Just like the method, find_residual
will not care if the edge is an outEdge or an inEdge as just needs to find a path and the corresponding pathMinCapacity.
As find_residual is finding a path we make sure that we are traversing both inEdges and outEdges by creating those edges along the way.
find_residual updates the remaining capacity we have to push so that we know when there are no more augmenting paths.
solve_network will care if the edge is an outEdge or inEdge in finding the final net flow of the network.
'''
import math


class Node:
    def __init__(self,label):
        '''
        Each node has a label, an inEdge list, and an outEdge list
        '''
        self.id = label
        self.outEdges = []
        self.inEdges = []


class Edge:
    def __init__(self,source, dest, capacity):
        '''

        :param source: Node type
        :param dest: Node type
        :param capacity: the capacity of the edge
        '''
        self.u = source
        self.v = dest
        self.edgeCapacity = capacity
        self.currentFlow = 0 # we set the current flow to 0



class Network:
    def __init__(self):
        '''
        creating a Network class
        '''
        self.labelToNode = {}
        self.nodeToLabel = {}
        # the two above dictionaries are used to just map the node to the label and are useful
        # since we may be handling a label or the actual Node object

        self.vertices = [] # a list of vertices
        self.edgeNodeList = {} # a vertex, in label form, will map to an adjacency list of neighbor vertices, again
        # in label form

        self.allEdgesList = [] # all edges as Edge objects

        self.flowEdges = {} # will hold the flows of outEdges and inEdges


        self.source = "S"
        self.target = "T"


    def add_node(self, label):
        '''

        :param label: the new vertex being added
        :return:
        '''
        # we add a vertex and we now create a new key to adjacency list
        self.vertices.append(label)

        # we also create the node object and make sure we have references to label and node
        node = Node(label)
        self.labelToNode[label] = node
        self.nodeToLabel[node] = label

    def add_edge(self,a,b,c):
        '''

        :param a: the src vertex in label form
        :param b: the dest vertex in label form
        :param c: the capacity of the edge
        :return:
        '''
        if c < 0: # INPUT CHECK
            print("Error in edge creation. Please check if capacity is positive integer")

        #if c == 0:
            #for i in range(len(self.allEdgesList)):
              #  if self.allEdgesList[i].v == a:
                   # self.allEdgesList[i].v = b

                    # if an edge has a has its destination then we shift to a's next which is b
                        # delete all edges of a
                        # look at all in edge and then set u's predeccesor to u next
                    #break

        # A owes B and C 1 dollar
        # B owes C and D 1 dollar


        if a not in self.labelToNode.keys():  # INPUT CHECK
            self.add_node(a)
        if b not in self.labelToNode.keys():
            self.add_node(b)

        # we create a directed edge between a and b
        # because this edge is a main edge as it is a part of the original graph
        # we will add it to the outEdges
        newEdge = Edge(a, b, c)
        if(self.getEdge(self.labelToNode[b], self.labelToNode[a]) == None):
            self.labelToNode[a].outEdges.append(newEdge)
        else:
            self.labelToNode[a].inEdges.append(newEdge)

        # we also update the list of allEdges
        self.allEdgesList.append(newEdge)



    def getEdge(self, u, v):
        '''

        :param u: the src node in label form
        :param v: the dest node in label form
        :return: the edge between (u,v) or None if not found
        '''
        for edge in self.allEdgesList:
            if edge.u == u and edge.v == v:
                return edge

    def find_residual(self, current, visited, minCapacity):
        '''

        :param current: the current vertex in label form
        :param visited: a list of visited vertices in label form that keeps track of vertices that have
        been explored in only this iteration
        :param minCapacity: the min capacity i.e how much we can push
        :return:
        '''

        # set the current vertex as visited and check if we have reached target, if not we
        # continue with our DFS
        visited[current] = "visited"
        if current == self.target:
            return minCapacity

        # to implement DFS with recursion we want to for each vertex to call DFS and keep exploring a path
        # to get to T, if we cannot we go back up the call stack to find another path
        for i in range(len(self.vertices)):

            # the "graph" we are looking at is the residual graph and we care more
            # about how much we push more so we focus on the remaining edge capacity

            # first we find if a path exists between current and the vertex we are looking
            # in getEdge we are looking through a list that has all edges both "in and out"
            # so when we when construct the residual networks and adding the reverse edges we will
            # be considering them.
            # However, we care if it is an in or outedge when examining the flow as we do in the
            # solve network, but here we just care about getting a path from S to T.

            pathEdge = self.getEdge(current, self.vertices[i])
            if pathEdge != None:
                # if we do have a path then we check 2 things: 1) is the dest vertex
                # already visited in this iteration 2) by checking the capacity we check if
                # we can push more through this edge. If the capacity is 0 that means that we can
                # not push more through this path THUS that the dest vertex is already is getting a max flow

                if (visited.get(self.vertices[i]) == None or visited[self.vertices[i]] != "visited")\
                    and (pathEdge.edgeCapacity != None
                                    and pathEdge.edgeCapacity > 0):


                    # if this edge is viable then we check if this is less than the previous path's
                    # capacity, if yes then we update

                    newMinCapacity = min(minCapacity, pathEdge.edgeCapacity)

                    # now we go further and find the neighbor of this neighbor vertex
                    # this is the recursive step

                    pathMinCapacity = self.find_residual(self.vertices[i], visited, newMinCapacity)

                    # after finishing the recursive step, if we did reach T we now know what the min capacity of the
                    # path is from this vertex to T. We also through the pathMinCapacity > 0
                    # prevent ourselves from getting an augmenting path that has already been explored and has
                    # already given the dest vertex a max flow

                    if pathMinCapacity != None and pathMinCapacity > 0:

                       # back to this edge we are going to increase the path's current flow in the main
                       # flow graph while decreasing the edge capacity in the resdiual graph since now
                       # we can only push edge capacity - amountPushed next time around

                        pathEdge.currentFlow = pathEdge.currentFlow + pathMinCapacity

                        # self.flowEdges is a data structure that holds the flows of BOTH main edges and
                       # reverse edges. This is critical as in solve network to find the final flow
                       # of each edge we will be finding the netFlow from that vertices out and in edges
                        self.flowEdges[pathEdge] = pathEdge.currentFlow

                        # we decrease the remaining capacity of stuff we can push
                        pathEdge.edgeCapacity = pathEdge.edgeCapacity - pathMinCapacity


                        # as stated in the program description our program while recursing and finding an
                       # augmenting path will create the reverse edges so here we check if 1) does the reverse edge
                       # already exist
                       #
                       # 2) if not then we add it so that when we do another iteration of finding a
                       # path from S to T we can use this reverse edge
                       #
                       # 2) if yes then since we decrease the complementary edge's remaining capacity
                       # we will increase the reverse edge's capacity
                       # for example if we push 1 package from A to B where the capacity from A to B is 1 then
                       # the edge between A to B will have a remaining capacity of 0 whereas from B to A now we
                       # can push 1 package thus incrementing the capacity of B to A

                        reverseEdge = self.getEdge(self.vertices[i], current)
                        if reverseEdge is None:
                            self.add_edge(self.vertices[i], current, pathMinCapacity)
                        else:
                            reverseEdge.edgeCapacity = reverseEdge.edgeCapacity + pathMinCapacity

                        return pathMinCapacity
        return -1 # if the dest node is visited or if we cannot push more through this edge return -1

    def solve_network(self):
        '''

        :return: will return the max flow and the path
        '''
        minCapacity = math.inf # we set the mincapacity to infinite because
        # we need to make sure that know what the actual min capacity is so that when we push we do
        # not violate a edge capacity
        maxFlow = 0

        visited = {} # a dictionary that will have the label as a key and the value will be if it is
        # visited or not
        while True:
            minCapacity = self.find_residual(self.source, visited, minCapacity) # keep finding augmenting paths
            # and their min capacity
            if minCapacity <= 0:
                # if our minCapacity is 0 that means that we cannot push more stuff and that we have reached the max
                # flow we can get into T so break
                break
            maxFlow = maxFlow + minCapacity # if we do a get a minCapacity that means this is what we can push
            # in our flow graph so we increase the flow to T
            visited = {} # we reset the visited and min capacity for the next iteration
            minCapacity = math.inf
        print(maxFlow)

        for key in self.flowEdges.keys():

            # self.flowEdges has all the edge's current flows in a dictionary format
            # of keys being the edge and the value being the edge capacity. It is created in
            # such a way to maintain organization

            # for each edge we check if it is an outEdge if so then this was a main edge from the orginal flow
            # graph and then we subtract that from the reverse edge to get what the edge in the main graph
            # is pushing
            flowEdge = key
            edgeStart = flowEdge.u
            edgeEnd = flowEdge.v

            if (flowEdge in self.labelToNode[edgeStart].outEdges and flowEdge.u != "S" and flowEdge.v != "T"):
                # we get the flow of the main edge
                net_flow = flowEdge.currentFlow
                reverse_edge = self.getEdge(edgeEnd, edgeStart)
                if (reverse_edge in self.flowEdges):
                    # we get the flow of the reverse edge
                    net_flow = net_flow - reverse_edge.currentFlow
                    # to then get the net flow of the edge in the flow network
                if (net_flow > 0):
                    print(edgeStart + " to " + edgeEnd + " with flow amount " + str(
                        net_flow))

