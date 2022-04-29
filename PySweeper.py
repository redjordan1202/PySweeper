#PySweeper -  tkinter based Minesweeper Clone
from tkinter import *
from vars import *


#Set up window and class for app
class App:
    def __init__(self, master):
        self.master = master
        master.title("PySweeper")

        self.frm_grid = Frame(master=master)
        self.frm_grid.pack()
        self.frm_grid.pack_propagate(0)

        self.blank_img = PhotoImage()
        self.draw_grid()

#Draw grid of buttons
    def draw_grid(self):
        #Using easy sized 9x9 grid for now
        for y in range(0, EASY_ROWS, 1):
            for x in range(0, EASY_COLS, 1):
                self.button = Button(master=self.frm_grid, 
                    bg='white',
                    width=TILE_SIZE,
                    height=TILE_SIZE,
                    image=self.blank_img,
                    relief='raised',
                    borderwidth=20
                )
                self.button.grid(column=x, row=y)

#Dynamic Window Size based on size of grid

#Draw status bar, adjust window to fit

#Remove Square on click

#Place Mines

#Gameover if Mine clicked on

#Display number on clicked Squares

#Place Flag and protect square

#Win once all non-mine squares are gone


if __name__ == "__main__":
    root = Tk()
    #Using this window size until we have function for window size
    root.geometry('500x500')
    mainApp = App(root)
    root.mainloop()