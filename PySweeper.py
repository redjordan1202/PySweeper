#PySweeper -  tkinter based Minesweeper Clone
from tkinter import *
from vars import *


#Set up window and class for app
class App:
    def __init__(self, master):
        self.master = master
        master.title("PySweeper")
        root.configure(bg=DARK_GREY)

#Set window to Easy size. Which is default
        self.set_win_size(1)
#blank image to allow pixel sizing on buttons
        self.blank_img = PhotoImage()
#list of grid buttons
        self.grid_btns = []

#define Status Bar widgets
        self.frm_status = Frame(master=master,
            height=STATUS_HEIGHT,
            width=(self.win_width-WIN_PADDING) * 2.5,
            bg=DARK_GREY,
            relief='sunken',
            borderwidth=8
        )
        self.btn_reset = Button(master=self.frm_status,
            image=self.blank_img,
            width=25,
            height=25,
            bg='yellow',
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

#Grid Frame
        self.frm_grid = Frame(master=master, 
            bg=DARK_GREY,
            relief='sunken',
            borderwidth=8,
        )


#Status Bar Drawing
        self.frm_status.pack(pady=10)
        self.frm_status.grid_propagate(0)
        self.frm_status.grid_columnconfigure(0, weight=1)
        self.frm_status.grid_columnconfigure(2, weight=1)
        self.frm_status.grid_rowconfigure(0, weight=1)
        self.frm_status.grid_rowconfigure(2, weight=1)
        self.ent_mine_count.grid(column=0, row=1, padx=5, pady=4)
        self.btn_reset.grid(column=1, row=1, pady=4)
        self.ent_score.grid(column=2, row=1, padx=5, pady=4)

# Grid Section Drawing
        self.frm_grid.pack()
        self.frm_grid.pack_propagate(0)        
        self.draw_grid()
        

#Draw grid of buttons
    def draw_grid(self):
        #Using easy sized 9x9 grid for now
        for y in range(0, EASY_ROWS, 1):
            rows = []
            for x in range(0, EASY_COLS, 1):
                self.button = Button(master=self.frm_grid, 
                    bg=DARK_GREY,
                    width=TILE_SIZE,
                    height=TILE_SIZE,
                    image=self.blank_img,
                    relief='raised',
                    borderwidth=5,
                    command=lambda row=y, col=x: self.check_btn(row,col),
                    compound='top'
                )
                rows.append(self.button)
                self.button.grid(column=x, 
                    row=y,
                    padx=2,
                    pady=2
                )
                self.frm_grid.columnconfigure(x,minsize=TILE_SIZE)
            self.frm_grid.rowconfigure(y,minsize=TILE_SIZE)
            self.grid_btns.append(rows)



#Dynamic Window Size based on difficulty
    def set_win_size(self, difficulty):
        #Custom = 0, Easy = 1, Intermediate = 2, Expert = 3
        if difficulty == 1:
            self.win_width = (EASY_ROWS * TILE_SIZE) + WIN_PADDING
            self.win_height = (EASY_ROWS * TILE_SIZE) + WIN_PADDING + STATUS_HEIGHT
            root.minsize(width=self.win_width, height=self.win_height)
            root.resizable(False,False)

#function to check if button clicked is mine or not
#also changes the appearance of the button. 
#right now just changes the appearance of the button
    def check_btn(self,row,col):
        active_btn = self.grid_btns[row][col]
        active_btn.configure(
            width=TILE_SIZE + 6,
            height=TILE_SIZE + 6,
            text='1',
            compound='center',
            relief='groove',
            borderwidth=1,
            font=('Terminal', 16),
            disabledforeground='blue',
            state='disabled'
        )
        
        





#Place Mines

#Gameover if Mine clicked on

#Display number on clicked Squares

#Place Flag and protect square

#Win once all non-mine squares are gone


if __name__ == "__main__":
    root = Tk()
    mainApp = App(root)
    root.mainloop()