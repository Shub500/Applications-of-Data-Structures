'''
Name: Shubham Mohole
Program Description: We have two classes: a maze class and a cell node class. The Maze class creates a 2D matrix
that is filled by cell node objects that are either rooms or corridors depending on the index. The Maze class also is the
class that initiates the DFS and it goes through each room and its neighbors and its neighbors until it reaches cells that
do not have unvisited neighbors, in which case it backtracks. All the while if we check if there is the possibility of
cycle being created and if there is one we create a wall between the cells. At the end then we color the maze
based on if it is a viable cell to walk in or not and we have buttons to either start over or quit.

'''




import random
import Lab08MazeGraphics
from graphics import *


class CellNode():
    def __init__(self, x, y, maze):
        '''

        :param x: the x cord
        :param y: the y cord
        :param maze: a copy of a maze
        '''

        self.i = x
        # the x cord of the cell

        self.j = y
        # the y cord of the cell
        self.previousCell = None
        # keeps track of its source cell that lead to this cell

        self.maze = maze
        # the maze matrix itself
        if x % 2 == 1 and y % 2 == 1:
            # if the indices are both odd that is a room
            self.type = "room"
            self.visitedRoomList = [False, False, False, False, False]
            # so the the 0 index = the source room, 1 index = top room, 2 index = bottom room, 3 index = right room
            # 4 index = left room
        else:
            # otherwise we have a corridor and we want to have a walkable instance variable
            self.type = "corridor"
            self.walkable = None

    def assignNeighRooms(self):
        '''

        :return: for each room cell it will have an instance variable of its top, bottom, right, and left room if it is exists
        '''
        if self.isIndexPossible(self.i - 2, self.j):
            self.topRoom = self.maze[self.i - 2][self.j]
        else:
            self.topRoom = False

        if self.isIndexPossible(self.i + 2, self.j):
            self.bottomRoom = self.maze[self.i + 2][self.j]
        else:
            self.bottomRoom = False

        if self.isIndexPossible(self.i, self.j + 2):
            self.rightRoom = self.maze[self.i][self.j + 2]
        else:
            self.rightRoom = False

        if self.isIndexPossible(self.i, self.j - 2):
            self.leftRoom = self.maze[self.i][self.j - 2]
        else:
            self.leftRoom = False

    def isIndexPossible(self, x, y):
        '''

        :param x: the x cords of the cell
        :param y: the y cords of the cell
        :return: if the cell exsits in the maze dimensions then this cell is possible
        '''
        if x > len(self.maze) - 1 or y > len(self.maze[x]) - 1 or x < 0 or y < 0:
            return False
        else:
            return True

    def getPossibleNeighbor(self):
        '''

        :param sourceRoom: type Cell Node that will have the x and y coordinates
        :return: returns a room that we will walk to
        '''

        movableAdjacentCells = []

        # the idea is that we check if the room exists and if it is not visited then we add to the possible neighbors

        if self.topRoom != False and self.visitedRoomList[1] == False and self.maze[self.i - 1][
            self.j].walkable != False: # we check if the room first exists, then if it exists and finally if the corridor
            # between the two rooms has not been walked through
            pair = []
            pair.append(self.topRoom) # we add the top room
            pair.append("top") # an indicator that it is the top as it will be helpful in marking the visited lists of the
            # two cells that the respective neighbors are vistied
            pair.append(self.i - 1) # these two lines are the cordinates for the corridor room
            pair.append(self.j)
            movableAdjacentCells.append(pair)

        if self.bottomRoom != False and self.visitedRoomList[2] == False and self.maze[self.i + 1][
            self.j].walkable != False:
            pair = []
            pair.append(self.bottomRoom)
            pair.append("bottom")
            pair.append(self.i + 1)
            pair.append(self.j)
            movableAdjacentCells.append(pair)

        if self.rightRoom != False and self.visitedRoomList[3] == False and self.maze[self.i][
            self.j + 1].walkable != False:
            pair = []
            pair.append(self.rightRoom)
            pair.append("right")
            pair.append(self.i)
            pair.append(self.j + 1)
            movableAdjacentCells.append(pair)

        if self.leftRoom != False and self.visitedRoomList[4] == False and self.maze[self.i][
            self.j - 1].walkable != False:
            pair = []
            pair.append(self.leftRoom)
            pair.append("left")
            pair.append(self.i)
            pair.append(self.j - 1)
            movableAdjacentCells.append(pair)

        if len(movableAdjacentCells) == 0: # we store all potential neighbors then randomly select a neighbor to go to
            return -1
        else:
            randomIndex = random.randint(0, len(movableAdjacentCells) - 1)
            return movableAdjacentCells[randomIndex]
        # will return three elements 1) the neighbor cell and the coordinates for the corridor cell being moved through
        # works

    def getNPWCorridors(self, visitedRooms):
        '''

        :param sourceRoom: for all the rooms that have been visited we are going to make the corridor between the visited room
        and the current room as not walkable to prevent a cycle to occur
        :return:
        '''

        # if the room is marked visited in our dictionary and the corridor between the current cell and that room
        # is not marked then we know that we may create a cycle which is not good, so we wall off that corridor by marking
        # it as false

        if self.topRoom:
            if visitedRooms[self.topRoom] == True and self.maze[self.i - 1][self.j].walkable == None:
                self.maze[self.i - 1][self.j].walkable = False

        if self.bottomRoom:
            if visitedRooms[self.bottomRoom] == True and self.maze[self.i + 1][self.j].walkable == None:
                self.maze[self.i + 1][self.j].walkable = False


        if self.rightRoom:
            if visitedRooms[self.rightRoom] == True and self.maze[self.i][self.j + 1].walkable == None:
                self.maze[self.i][self.j + 1].walkable = False


        if self.leftRoom:
            if visitedRooms[self.leftRoom] == True and self.maze[self.i][self.j - 1].walkable == None:
                self.maze[self.i][self.j - 1].walkable = False


class Maze():
    def __init__(self, length, width):
        '''

        :param length: the length of the maze
        :param width: the width of the maze
        '''
        self.mazeMatrix = [[None] * (2 * length + 1) for i in range(2 * width + 1)]
        self.currentCell = None # keeps track of current cell
        self.end = None
        self.visitedCells = {} # a dictionary of cells if they have been visited or not

    def fillMaze(self):
        '''

        :return: this will return a maze of cell nodes that if applicable will have references to its neighbors as
        well as call the DFS method to determine the paths of the maze
        '''
        for r in range(len(self.mazeMatrix)): # fills the maze with cells that have not been visited
            for c in range(len(self.mazeMatrix[r])):
                newCell = CellNode(r, c, None)
                self.mazeMatrix[r][c] = newCell
                self.visitedCells[self.mazeMatrix[r][c]] = False

        self.currentCell = self.mazeMatrix[1][1] # starts at the 1,1 cell the leftmost possible room

        for r in range(len(self.mazeMatrix)): # with the completed maze each cell object will have a copy of it as well as
            # we are going to assign its neighbors
            for c in range(len(self.mazeMatrix[r])):
                self.mazeMatrix[r][c].maze = self.mazeMatrix
                self.mazeMatrix[r][c].assignNeighRooms()



        if len(self.mazeMatrix) % 2 == 0:
            if len(self.mazeMatrix[0]) % 2 == 0:
                end = self.mazeMatrix[len(self.mazeMatrix) - 1][len(self.mazeMatrix[0]) - 1]
            else:
                end = self.mazeMatrix[len(self.mazeMatrix) - 1][len(self.mazeMatrix[0]) - 2]
        else:
            if len(self.mazeMatrix[0]) % 2 == 0:
                end = self.mazeMatrix[len(self.mazeMatrix) - 2][len(self.mazeMatrix[0]) - 1]
            else:
                end = self.mazeMatrix[len(self.mazeMatrix) - 2][len(self.mazeMatrix[0]) - 2]

            self.end = end
            self.moveCellDFS() # calls our recursive function

    def moveCellDFS(self):
        '''

        :return: the idea of this function is that at the current cell we find the potential neighbor room cells that we c
        can go to which basically means if that room is unvisited we can go it. If we do have a potential next room
        we go to that room and each cell's visited neighbors list is marked true in the respective index. We then also
        look at if we may be creating cycles: an example: A - B
                                                              |
                                                          D  - C

        Here A is already visited but in D's visited list that is not reflected so D could go to A creating a cycle. However
        by having the maze visited nodes dictionary we know that because A is visited and D does not have that registered
        that we should add a wall.

        We then set the next room to the current cell and recurse.

        If we do not have any neighbors we back track by relying on the previous cell attribute all the cell nodes have
        which is basically the cell that lead to the current cell. By then setting the current cell as the previous cell of the
        source node we back track and try to find a potential neighbor. This keeps happening until we get to a cell
        whose previous cell is None and that signals that we are back at square 1 (both literally and figuratively).

        We then color the grid at the end by calling the coloring function

        current cell in the maze to the next room.
        '''
        sourceCell = self.currentCell # we keep track the current cell
        sourceCell.visitedRoomList[0] = True # we mark it as visited
        self.visitedCells[sourceCell] = True # we mark in our maze dictionary that this cell is visited

        nextInfo = sourceCell.getPossibleNeighbor() # we get the info about our next move

        if nextInfo == -1: # if we do not have any next rooms we go backwards by calling upon the previous cell of the cell node
            # that lead to this cell
            self.currentCell = sourceCell.previousCell
            if self.currentCell == None: # if we are back at the start we print the maze
                self.printMaze()
                return True

        else:
            nextRoom = nextInfo[0] # otherwise we have a next room and this room cell will have the current cell as its
            # previous cell
            nextRoom.previousCell = sourceCell
            # now if each of the cell's visited list we make the designated neighbor cell true
            if nextInfo[1] == "top":
                sourceCell.visitedRoomList[1] = True
                nextRoom.visitedRoomList[2] = True
            elif nextInfo[1] == "bottom":
                sourceCell.visitedRoomList[2] = True
                nextRoom.visitedRoomList[1] = True
            elif nextInfo[1] == "right":
                sourceCell.visitedRoomList[3] = True
                nextRoom.visitedRoomList[4] = True
            elif nextInfo[1] == "left":
                sourceCell.visitedRoomList[4] = True
                nextRoom.visitedRoomList[3] = True

            corridorBetweenRoom = self.mazeMatrix[nextInfo[2]][nextInfo[3]]
            # get the corridor between current and next and mark as true
            corridorBetweenRoom.walkable = True

            # we then check if we potentially might have cycle and we wall off
            nextRoom.getNPWCorridors(self.visitedCells)
             # set the current cell to the next room
            self.currentCell = nextRoom
        # we recurse again on this nextRoom or previousRoom
        self.moveCellDFS()


    def printMaze(self):
        '''

        :return: returns a maze that has the * as rooms  " " spaces as walkable corridors and | as walls
        '''
        for row in self.mazeMatrix:
            for element in row:
                if element.type == "corridor":
                    if element.walkable == False or element.walkable == None:
                        print("|", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print("*", end=" ")
            print()

    def colorMaze(self):
        '''

        :return: we create maze gui and by scaling the indcies up and still using the attributes of the maze we add color
        to the maze by adding red to cells that cannot be navigated and green to cells that can
        '''
        self.maze = Lab08MazeGraphics.MazeGUI(len(self.mazeMatrix), len(self.mazeMatrix[0]))
        for row in range(len(self.mazeMatrix)):
            for col in range(len(self.mazeMatrix[row])):

                # values are cellNodes, rooms are self.type = 'room'
                # walls are self.type = 'corridor', self.walkable

                if self.mazeMatrix[row][col].type == "corridor":
                    if self.mazeMatrix[row][col].walkable == False or self.mazeMatrix[row][col].walkable == None:
                        self.maze.fillCell(row, col, 'red')
                    else:
                        self.maze.fillCell(row, col, 'green')
                else:
                    self.maze.fillCell(row, col, 'green')


def main():
    '''
    Code Done By: Marie-Anne

    :return: in the first pass the user enters a valid maze height and width and if they do enter valid numbers we create
    the maze. The user also has buttons play again and quit. By using while loop variables if the user clicks play again
    another window will open with a new sequence of questions asking the dimensions of the maze. Quit deletes all windowss
    of the game and can only be pressed on the original window.
    '''
    quit = True
    while quit:
        mazeWidth = eval(input('Enter the width of the maze: ')) # we ask for viable dimensions
        if mazeWidth <= 0:
            mazeWidth = eval(input('Error, Invalid Input. Enter the width of the maze: '))
        while mazeWidth <= 0 and mazeWidth % 1 != 0:
            mazeWidth = eval(input('Enter a positive integer: '))
        mazeHeight = eval(input('Enter the height of the maze: '))
        if mazeHeight <= 0:
            mazeHeight = eval(input('Error, Invalid Input. Enter the height of the maze: '))
        while mazeHeight <= 0 and mazeHeight % 1 != 0:
            mazeHeight = eval(input('Enter a positive integer: '))

        maze = Maze(mazeWidth, mazeHeight) # we create the maze

        quit = maze.fillMaze() # we call upon the maze to fill and if we are done filling the quit returns True
        maze.colorMaze()

        pt = maze.maze.getMouse()
        buttonNotClicked = True
        while buttonNotClicked:

            if maze.maze.quitClicked(pt) == True: # if the quit button is clicked we quit
                while maze.maze.window:
                    maze.maze.quitWindow()

            elif maze.maze.newMazeClicked(pt) == True: # if the play again button is clicked we exit this loop
                # and re run the top of this method

                print('new maze clicked')
                buttonNotClicked, quit = False, True
            else:
                pt = maze.maze.getMouse()


main()
