#PySweeper -  tkinter based Minesweeper Clone
from tkinter import *
from vars import *
import random

class GridButton(Button):
    def __init__(self, master, row, col, mine_count, *args, **kwargs):
        Button.__init__(self, master, *args, **kwargs)
        self.row = row
        self.col = col
        self.mine_count = mine_count

        self.adjacent_cells = []
        self.adjacent_cells.append((self.row+1, self.col))
        self.adjacent_cells.append((self.row, self.col+1))
        self.adjacent_cells.append((self.row-1, self.col))
        self.adjacent_cells.append((self.row, self.col-1))
        self.adjacent_cells.append((self.row+1, self.col+1))
        self.adjacent_cells.append((self.row-1, self.col-1))
        self.adjacent_cells.append((self.row+1, self.col-1))
        self.adjacent_cells.append((self.row-1, self.col+1))

    def get_mine_count(self):
        for cell in self.adjacent_cells:
            if cell in mainApp.mines:
                self.mine_count += 1

    def update_cell(self):
        if self.mine_count == 0:
            text = ""
        else:
            text = str(self.mine_count)
        self.configure(
            width=TILE_SIZE,
            height=TILE_SIZE,
            text= text,
            compound='center',
            relief='groove',
            borderwidth=1,
            font=('Terminal', 10),
            foreground=self.get_color(),
        )
    
    def get_color(self):
        color = 'black'
        match self.mine_count:
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
        return color





#Set up window and class for app
class App:
    def __init__(self, master):
        self.master = master
        master.title("PySweeper")
        root.configure(bg=DARK_GREY)

#Set window to Easy size. Which is default
        self.set_win_size(1)
#images
        self.img_blank = PhotoImage()
        self.img_mine = PhotoImage(file = MINE)
        self.img_smile = PhotoImage(file=SMILE)
        self.img_dead = PhotoImage(file=DEAD)
        self.img_flag = PhotoImage(file=FLAG)
#cord lists
        self.grid_btns = []
        self.mines = []
        self.flags = []
        self.cleared_space = []

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
            image=self.img_smile,
            width=40,
            height=40,
            bg=DARK_GREY,
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
                self.button = GridButton(master=self.frm_grid, 
                    bg=DARK_GREY,
                    width=TILE_SIZE,
                    height=TILE_SIZE,
                    image=self.img_blank,
                    relief='raised',
                    borderwidth=2,
                    command=lambda row=y, col=x: self.get_cords(row,col),
                    compound='top',
                    activebackground = DARK_GREY,
                    row = y,
                    col = x,
                    mine_count = 0,
                )
                self.button.active = 1

                rows.append(self.button)
                self.button.grid(column=x, 
                    row=y,
                    padx=2,
                    pady=2
                )
                self.button.bind("<Button-2>", 
                    lambda event=None, row=y, col=x: self.place_flag(event, row, col)
                )
                self.button.bind("<Button-3>", 
                    lambda event=None,row=y, col=x: self.place_flag(event, row, col)
                )
                self.frm_grid.columnconfigure(x,minsize=TILE_SIZE)
            self.frm_grid.rowconfigure(y,minsize=TILE_SIZE)
            self.grid_btns.append(rows)

    def place_flag(self, event, row, col):
        selection = (row, col)
        if selection in self.cleared_space:
            return
        if selection in self.flags:
            self.grid_btns[selection[0]][selection[1]].configure(
                image= self.img_blank,
            )
            self.grid_btns[selection[0]][selection[1]].active = 1
            self.flags.remove(selection)
        else:
            self.grid_btns[selection[0]][selection[1]].configure(
                image= self.img_flag,
            )
            self.grid_btns[selection[0]][selection[1]].active = 0
            self.flags.append(selection)


#Dynamic Window Size based on difficulty
    def set_win_size(self, difficulty):
        #Custom = 0, Easy = 1, Intermediate = 2, Expert = 3
        if difficulty == 1:
            self.win_width = (EASY_ROWS * TILE_SIZE) + WIN_PADDING
            self.win_height = (EASY_ROWS * TILE_SIZE) + WIN_PADDING + STATUS_HEIGHT
            root.minsize(width=self.win_width, height=self.win_height)
            root.resizable(False,False)

#function to get and check cords of clicked button
#pass cords to other functions based on if mine or not
    def get_cords(self,row,col):
        selection = (row, col)
        if self.grid_btns[selection[0]][selection[1]].active == 0:
            return
        else:
            if self.click_count == 0:
                self.place_mines(selection)
                
            if selection in self.mines:
                self.hit_mine(selection)
                return

            self.update_cell(selection)
            self.click_count += 1
            self.cleared_space.append(selection)

#Checks for nearby mines, updates cell number.
    def update_cell(self,selection):
        active_btn = self.grid_btns[selection[0]][selection[1]]
        active_btn.update_cell()
        active_btn.active = 0

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
            else:
                row = random.randrange(0,EASY_ROWS)
                col = random.randrange(0,EASY_COLS)
                mine = (row, col)
                self.mines.append(mine)
        for row in self.grid_btns:
            for button in row:
                button.get_mine_count()
                print(button.mine_count)

    def hit_mine(self,selection):
        hit_mine = self.grid_btns[selection[0]][selection[1]]
        hit_mine.configure(
                width=TILE_SIZE,
                height=TILE_SIZE,
                compound='center',
                relief='groove',
                borderwidth=1,
                image = self.img_mine,
                bg = RED,
                activebackground = RED
            )
        for mine in self.mines:
                if mine == selection:
                    continue
                else:
                    active_btn = self.grid_btns[mine[0]][mine[1]]
                    active_btn.configure(
                        width=TILE_SIZE,
                        height=TILE_SIZE,
                        compound='center',
                        relief='groove',
                        borderwidth=1,
                        image = self.img_mine,
                    )
        for row in self.grid_btns:
                for button in row:
                    #button.config(state = 'disabled')
                    button.active = 0
                    button.unbind("<Button-2>")
                    button.unbind("<Button-3>")
        self.btn_reset.configure(image= self.img_dead)

#Win once all non-mine squares are gone









if __name__ == "__main__":
    root = Tk()
    mainApp = App(root)
    root.mainloop()