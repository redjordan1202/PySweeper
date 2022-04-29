#PySweeper -  tkinter based Minesweeper Clone
from tkinter import *
from vars import *


#Set up window and class for app
class App:
    def __init__(self, master):
        self.master = master
        master.title("PySweeper")
        root.configure(bg=DARK_GREY)

        #creating a blank image to allow pixel sizing on buttons
        self.blank_img = PhotoImage()


        #Draw status bar
        self.frm_status = Frame(master=master,
            height=60,
            width=250,
            bg=DARK_GREY,
            relief='sunken',
            borderwidth=5
        )
        self.btn_reset = Button(master=self.frm_status,
            image=self.blank_img,
            width=25,
            height=25,
            bg='yellow'
        )
        self.ent_mine_count = Entry(master=self.frm_status,
            state='disabled',
            font=('Arial', 24),
            disabledbackground='black'
        )
        self.ent_score = Entry(master=self.frm_status,
            state='disabled',
            font=('Arial', 24),
            disabledbackground='black'
        )

        self.frm_status.pack(pady=10)
        self.frm_status.grid_propagate(0)
        self.frm_status.grid_columnconfigure(0, weight=1)
        self.frm_status.grid_columnconfigure(2, weight=1)
        self.frm_status.grid_rowconfigure(0, weight=1)
        self.frm_status.grid_rowconfigure(2, weight=1)
        self.ent_mine_count.grid(column=0, row=1, padx=5)
        self.btn_reset.grid(column=1, row=1)
        self.ent_score.grid(column=2, row=1, padx=5)


        #Drawing Frame around button grid
        self.frm_grid = Frame(master=master, 
            bg=DARK_GREY,
            relief='sunken',
            borderwidth=5
        )
        self.frm_grid.pack()
        self.frm_grid.pack_propagate(0)

        
        self.draw_grid()
        

#Draw grid of buttons
    def draw_grid(self):
        #Using easy sized 9x9 grid for now
        for y in range(0, EASY_ROWS, 1):
            for x in range(0, EASY_COLS, 1):
                self.button = Button(master=self.frm_grid, 
                    bg=DARK_GREY,
                    width=TILE_SIZE,
                    height=TILE_SIZE,
                    image=self.blank_img,
                    relief='raised',
                    borderwidth=5,
                )
                self.button.grid(column=x, 
                    row=y,
                    padx=2,
                    pady=2
                )

#Dynamic Window Size based on size of grid



#Remove Square on click

#Place Mines

#Gameover if Mine clicked on

#Display number on clicked Squares

#Place Flag and protect square

#Win once all non-mine squares are gone


if __name__ == "__main__":
    root = Tk()
    #Using this window size until we have function for window size
    root.geometry('300x400')
    mainApp = App(root)
    root.mainloop()