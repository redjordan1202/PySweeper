#PySweeper -  tkinter based Minesweeper Clone
from tkinter import *
from vars import *
import random


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
#mine image
        self.img_mine = PhotoImage(file = MINE)
#list of grid buttons
        self.grid_btns = []
# Mines
        self.mines = []
#Count of clicks. Right now only used to prevent the player losing on their first click
        self.click_count = 0
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
        self.ent_mine_count.grid(column=0, row=1, padx=5, pady=4,sticky=W)
        self.btn_reset.grid(column=1, row=1, pady=4)
        self.ent_score.grid(column=2, row=1, padx=5, pady=4,sticky=E)

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
#right now just changes the appearance of the buttons
    def check_btn(self,row,col):
        selection = (row, col)
        if self.click_count == 0:
            self.place_mines(selection)

        if selection in self.mines:
            self.hit_mine(selection)
            return

        else:
            mine_count = 0
            # COL + 1
            selection = (row, col - 1)
            if selection in self.mines:
                mine_count += 1
            #COL - 1
            selection = (row, col + 1)
            if selection in self.mines:
                mine_count += 1
            #ROW + 1
            selection = (row + 1, col)
            if selection in self.mines:
                mine_count += 1
            #ROW -1
            selection = (row - 1, col)
            if selection in self.mines:
                mine_count += 1
            #ROW + 1 COL + 1
            selection = (row + 1, col + 1)
            if selection in self.mines:
                mine_count += 1
            #ROW + 1 COL -1
            selection = (row + 1, col - 1)
            if selection in self.mines:
                mine_count += 1
            #ROW - 1 COL -1
            selection = (row - 1, col - 1)
            if selection in self.mines:
                mine_count += 1
            #ROW - 1 COL + 1
            selection = (row - 1, col + 1)
            if selection in self.mines:
                mine_count += 1
            if mine_count == 0:
                mine_count = ""

            color = 'black'
            match mine_count:
                case 1:
                    color = BLUE
                case 2:
                    color = GREEN
                case 3:
                    color = RED
                case 4:
                    color = DARK_BLUE
                case 5:
                    color = DARK_RED
                case 6:
                    color = TEAL
                case 7:
                    color = BLACK
                case 8:
                    color = GREY

            active_btn = self.grid_btns[row][col]
            active_btn.configure(
                width=TILE_SIZE + 6,
                height=TILE_SIZE + 6,
                text= str(mine_count),
                compound='center',
                relief='groove',
                borderwidth=1,
                font=('Terminal', 16),
                disabledforeground=color,
                state='disabled'
            )
            self.click_count += 1
        
        
#Place Mines
    def place_mines(self, selection):
        safe_click = False
        while safe_click == False:
            for x in range(EASY_MINES):
                row = random.randrange(0,EASY_ROWS)
                col = random.randrange(0,EASY_COLS)
                mine = (row, col)
                self.mines.append(mine)
            if selection in self.mines:
                continue
            else:
                safe_click = True
                break

        mines_verified = False
        while mines_verified != True:
            self.mines = list(set([i for i in self.mines]))
            if len(self.mines) == EASY_MINES:
                mines_verified = True
                for mine in self.mines:
                    print(mine)
            else:
                print("Rerolling Mines")
                row = random.randrange(0,EASY_ROWS)
                col = random.randrange(0,EASY_COLS)
                mine = (row, col)
                self.mines.append(mine)

    def hit_mine(self,selection):
        hit_mine = self.grid_btns[selection[0]][selection[1]]
        hit_mine.configure(
                width=TILE_SIZE + 6,
                height=TILE_SIZE + 6,
                compound='center',
                relief='groove',
                borderwidth=1,
                image = self.img_mine,
                state = 'disabled',
                bg = RED
            )
        for mine in self.mines:
                if mine == selection:
                    continue
                else:
                    active_btn = self.grid_btns[mine[0]][mine[1]]
                    active_btn.configure(
                        width=TILE_SIZE + 6,
                        height=TILE_SIZE + 6,
                        compound='center',
                        relief='groove',
                        borderwidth=1,
                        image = self.img_mine,
                        state = 'disabled',

                    )
        for row in self.grid_btns:
                for button in row:
                    button.configure(state = 'disabled')















#Gameover if Mine clicked on

#Display number on clicked Squares

#Place Flag and protect square

#Win once all non-mine squares are gone


if __name__ == "__main__":
    root = Tk()
    mainApp = App(root)
    root.mainloop()