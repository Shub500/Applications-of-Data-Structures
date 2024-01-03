
from graphics import *
from MinesweeperGUI import MinesweeperGUI
import random

class Minesweeper:

    def __init__(self):

        self.grid = []
        for i in range(8):
            self.grid.append([0]*8)
        self.mineCoords = []

    def makeGrid(self):
        """
        Randomly picks 10 cells to be mines and fills in clues based on the mines.
        Returns: None
        """
        mines = 0
        while mines < 10:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if (row, col) not in self.mineCoords:
                mines += 1
                self.mineCoords.append((row, col))
                self.grid[row][col] = -1

        # print(self.mineCoords)
        # for line in self.grid:
        #     print(line)

    def addClues(self):
        """
        Adds the clues based on the coordinates of the mines.
        """
        for mine in self.mineCoords:
            # self.grid[mine[1]][mine[0]] -= 1
            if mine[0] < 7: # not on the bottom row
                if self.grid[mine[0] + 1][mine[1]] != -1:
                    self.grid[mine[0] + 1][mine[1]] += 1 # bottom

                if mine[1] < 7 and self.grid[mine[0] + 1][mine[1] + 1] != -1: # top row, not right column
                    self.grid[mine[0] + 1][mine[1] + 1] += 1 # bottom right
                if mine[1] > 0 and self.grid[mine[0] + 1][mine[1] - 1] != -1: # top row, right column
                    self.grid[mine[0] + 1][mine[1] - 1] += 1 # bottom left


            if mine[0] > 0: # not on top row
                if self.grid[mine[0] - 1][mine[1]] != -1:
                    self.grid[mine[0] - 1][mine[1]] += 1 # top

                if mine[1] > 0 and self.grid[mine[0] - 1][mine[1] - 1] != -1: # bottom row, not left column
                    self.grid[mine[0] - 1][mine[1] - 1] += 1 # top left
                if mine[1] < 7 and self.grid[mine[0] - 1][mine[1] + 1] != -1: # bottom left corner case
                    self.grid[mine[0] - 1][mine[1] + 1] += 1 # top right
                

            if mine[1] < 7 and self.grid[mine[0]][mine[1] + 1] != -1: # not on right column
                self.grid[mine[0]][mine[1] + 1] += 1 # right
            if mine[1] > 0 and self.grid[mine[0]][mine[1] - 1] != -1: # not on left column
                self.grid[mine[0]][mine[1] - 1] += 1 # left


            # self.grid[mine[0] + 1][mine[1] + 1] += 1 # bottom right
            # self.grid[mine[0] + 1][mine[1] - 1] += 1 # bottom left
            # self.grid[mine[0] - 1][mine[1] + 1] += 1 # top right
            # self.grid[mine[0] - 1][mine[1] - 1] += 1 # top left

    def getNeighbors(self, row, col):
        """
        row = the grid x-coordinate (0 to 7) of the selected cell
        col = the grid y-coordinate (0 to 7)
        Returns a dictionary of coordinate (x, y) to clue
        """
        
        neighbors = {}

        if 0 <= row < 7: # not bottom row
            neighbors[(row + 1, col)] = self.grid[row + 1][col] # bottom
            if 0 <= col < 7:
                neighbors[(row + 1, col + 1)] = self.grid[row + 1][col + 1] # bottom right
            if 0 < col <= 7:
                neighbors[(row + 1, col - 1)] = self.grid[row + 1][col - 1] # bottom left

        if 0 < row <= 7:
            neighbors[(row - 1, col)] = self.grid[row - 1][col] # top
            if 0 <= col < 7:
                neighbors[(row - 1, col + 1)] = self.grid[row - 1][col + 1] # top right
            if 0 < col <= 7:
                neighbors[(row - 1, col - 1)] = self.grid[row - 1][col - 1] # top left


        if 0 <= col < 7: 
            neighbors[(row, col + 1)] = self.grid[row][col + 1] # right

        if 0 < col <= 7:
            neighbors[(row, col - 1)] = self.grid[row][col - 1] #left

        return neighbors
        
    def getMouse(self, gui):
        """
        Gets a mouse click from the user; if Quit is clicked, this function will automatically
        close the window. Returns the coordinates clicked otherwise.
        """
        gui.selectSquare()
        pt = gui.getMouse()
        validClick = False
        
        while validClick == False:
        # if Quit button clicked
            if gui.quitClicked(pt) == True:
                gui.quitGame()
            else:
                if 110 <= pt.getY() < 750:
                    row = int((pt.getY() - 30)//80 - 1)
                else: row = -1
                if 50 <= pt.getX() < 690:
                    col = int((pt.getX() + 30)//80 - 1)
                else: col = -1
            
            if row >= 0 and col >= 0:

                # TODO: infinite loop when a flag is clicked
                if (isinstance(gui.getButton(row, col).getLabel(), Polygon) == True or 
                    gui.getButton(row, col).clicked(pt) == True):
                    return row, col
            else:
                pt = gui.getMouse()

    def getKey(self, gui, row, col):
        """
        Gets a key from the user: 
        If 'f' (for 'flag') is clicked, then the square is flagged
        If 'd' (for 'dig') is clicked, then the clue(s) are revealed
        """
        gui.digOrFlag()
        key = gui.getWin().getKey()
        button = gui.getButton(row, col)

        while True:
            if key == 'f':

                if button.isActive() == True:
                    # flag selected cell at row, col
                    button.flag()
                elif isinstance(button.getLabel(), Polygon) == True:
                    button.reset()
                break

            elif key == 'd':
                clue = self.grid[row][col]
                # if not a mine: dig selected cell at row, col
                if clue > -1:
                    self.showClue(gui, row, col)
                    gui.getButton(row, col).setStatus()
                    if clue > 0:
                        gui.getButton(row, col).setStatus()
                    elif clue == 0:
                        self.noBombs(gui, row, col)
                else:
                    self.showMines(gui)
                    gui.gameOver()
                break
            else:
                key = gui.getWin().getKey()

    def showClue(self, gui, row, col):
        """
        Reveals the clue at row, col
        """
        button = gui.getButton(row, col)
        button.showClue(self.grid[row][col])

    def showMines(self, gui):
        for mine in self.mineCoords:
            button = gui.getButton(mine[0], mine[1])
            button.reset()
            button.setLabel(-1)

    def noBombs(self, gui, row, col):
        """
        Called when the cell at row, col has no mines around it.
        Uses BFS
        """
        zeros = [(row, col)]

        while zeros != []:

            neighbors = self.getNeighbors(zeros[0][0], zeros[0][1])

            for cell in neighbors:

                # shows all neighbors around first empty cell (layer 1)
                self.showClue(gui, cell[0], cell[1])

                # tracks neighbors that are 0 and visitable from row, col
                if neighbors[cell] == 0 and gui.getButton(cell[0], cell[1]).checkStatus() < 2:
                    zeros.append(cell)
                    gui.getButton(cell[0], cell[1]).setStatus()

            zeros.remove(zeros[0])

    def playGame(self, gui):

            # generate a grid
            self.makeGrid()
            self.addClues()
            
            for line in self.grid:
                print(line)

            gameOver = False

            # end condition: all squares w/o mines have been dug
            while gameOver == False: 

                # get a mouse click
                row, col = self.getMouse(gui)

                # highlight the square in the gui
                gui.getButton(row, col).highlight()

                # get key click
                self.getKey(gui, row, col)
                gui.getButton(row, col).unhighlight()

                
                # TODO: not allowing multiple moves
                gameOver = gui.isGameOver()

# minesweeper = Minesweeper()
# gui = MinesweeperGUI()
# minesweeper.makeGrid()
# minesweeper.addClues()
# for line in minesweeper.grid:
#     print(line)
# print(minesweeper.getNeighbors(3, 4))
# # print(minesweeper.mineCoords)
# minesweeper.showClue(gui, 4, 3)

# # CLICK & SHOW CLUE
# row, col = minesweeper.getMouse(gui)
# print(row, col)
# # minesweeper.showClue(gui, row, col)
# gui.getButton(row, col).highlight()
# gui.digOrFlag()
# minesweeper.getKey(gui, row, col)
# gui.getButton(row, col).unhighlight()

# minesweeper.getMouse(gui)
# minesweeper.showMines(gui)
# gui.reset()


def main():

    gui = MinesweeperGUI()

    while True:

        minesweeper = Minesweeper()
        minesweeper.playGame(gui)

        gui.gameOver()
        pt = gui.getMouse()
        while True:
            if gui.quitClicked(pt) == True:
                gui.quitGame()
            elif gui.playAgainClicked(pt) == True:
                gui.reset()
                break
            else:
                pt = gui.getMouse()


main()

