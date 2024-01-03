
from graphics import *
from MinesweeperButton import Button

class MinesweeperGUI:

    def __init__(self):

        # self.grid = [[0]*8]*8
        self.win = GraphWin("Minesweeper", 740, 800)

        self.message = Text(Point(375, 50), 'Welcome to Minesweeper! Click anywhere to start.')
        self.message.draw(self.win)

        self.squareToButton = {}
        for col in range(1, 9):
            for row in range(1, 9):
                x = (col-1)*80 + 90
                y = (row-1)*80 + 150
                self.squareToButton[(col, row)] = Button(self.win, 
                                                         Point(x, y), 80, 80, 'white', "")

        self.quit = Button(self.win,Point(130, 50), 75, 50, 'white', "Quit")
        self.quit.activate()

        self.playAgain = Button(self.win,Point(610, 50), 75, 50, 'white', "Play Again")

    def getWin(self):
        return self.win

    def getMouse(self):
        return self.win.getMouse()

    def reset(self):
        self.message.setText('Welcome to Minesweeper! Click anywhere to start.')
        self.quit.activate()
        self.playAgain.deactivate()

    def gameOver(self):
        self.message.setText('Click Quit to exit, or Play Again to restart.')
        self.playAgain.activate()

    def setMessage(self, message):
        """Display messages to the GUI."""
        self.message.setText(message)

    def showClue(self, x, y, clue):
        Text(Point(x, y), str(clue)).draw(self.win)

    def quitClicked(self, pt):
        """Returns whether or not the Quit button is clicked."""
        return self.quit.clicked(pt)

    def playAgainClicked(self, pt):
        """Returns whether or not the Play Again button is clicked."""
        return self.playAgain.clicked(pt)

gui = MinesweeperGUI()
gui.win.getMouse()
