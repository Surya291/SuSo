from tkinter import *
import numpy as np
from tkinter import ttk
import tkinter.font as font
class UI:
    def __init__(self,maze):
        self.maze = maze
        self.times = 0
    def createGUI(self):
        def alert_popup(title, message, path):
            """Generate a pop-up window for special messages."""
            root = Tk()
            root.title(title)
            w = 400  # popup window width
            h = 200  # popup window height
            sw = root.winfo_screenwidth()
            sh = root.winfo_screenheight()
            x = (sw - w) / 2
            y = (sh - h) / 2
            root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            m = message
            m += '\n'
            m += path
            w = Label(root, text=m, width=120, height=10)
            w.pack()
            b = Button(root, text="OK", command=root.destroy, width=10)
            b.pack()
            mainloop()


        def Suso(top, sud):
            k = [0, 0]
            if (not unassigned(sud, k)):
                return True

            r = k[0]
            c = k[1]
            i = 0
            for num in range(1, 10):
                if (is_safe(sud, r, c, num)):
                    sud[r][c] = num
                    print_maze(sud)
                    top.update()
                    top.after(10)


                    if Suso(top, sud):
                        return True
                    sud[r][c] = 0
            return False

        def unassigned(sud, k):
            for r in range(0, 9):
                for c in range(0, 9):
                    if (sud[r][c] == 0):
                        k[0] = r
                        k[1] = c
                        return True
            return False

        def check_in_row(sud, r, num):
            for c in range(0, 9):
                if (sud[r][c] == num):
                    return True
            return False

        def check_in_col(sud, c, num):
            for r in range(0, 9):
                if (sud[r][c] == num):
                    return True
            return False

        def check_in_grid(sud, r, c, num):
            row = r - (r % 3)
            col = c - (c % 3)
            for a in range(row, row + 3):
                for b in range(col, col + 3):
                    if (sud[a][b] == num):
                        return True
            return False

        def is_safe(sud, r, c, num):
            return (not (check_in_grid(sud, r, c, num)) and (not (check_in_row(sud, r, num))) and (
                not (check_in_col(sud, c, num))))

        #######################################################
        entries = []

        def initialize(top, arr):
            E = entries[0]

            m = 1
            for i in range(9):
                for j in range(9):
                    if (not E.get()):
                        arr[i][j] = 0
                    else:
                        arr[i][j] = int(E.get())
                    if (m <= 80):
                        E = entries[m]
                        m += 1

        def print_maze(arr):
            clean_Mess()
            E = entries[0]
            m = 1
            for i in range(9):
                for j in range(9):
                    if (arr[i][j] != 0):
                        E.insert(1, int(arr[i][j]))
                    if (m <= 80):
                        E = entries[m]
                        m += 1


        def launch_maze(top,arr):
            myFont = font.Font(family='Times', size=30, weight="bold")
            if(self.times>0):
                initialize(top, arr)
                print(arr)
            clean_Mess()
            same = valid_sud(arr)
            E = entries[0]

            e = 0
            f = 1
            for i in range(9):
                for j in range(9):
                    if (arr[i][j] != 0):
                        #print(i,j)
                        E.config(font=myFont, fg="red", justify='center')
                        E.insert(1, int(arr[i][j]))

                        if( (e<len(same) and (i,j) == same[e] )):
                            E.config(background = 'red',fg = "black")

                            e = e+1


                    if (f <= 80):
                        E = entries[f]
                        f += 1
            self.times = self.times+1
            print("LAUNCH HAS BEEN PRESSED :",self.times)

        def clean_Mess():
            for e in entries:
                e.delete(0, END)
                e.config(background = 'white')


        def valid_sud(maze):
            same = []
            for r in range(0, 9):
                for c in range(0, 9):
                    if (maze[r][c] != 0):

                        temp = maze[r][c]
                        maze[r][c] = 0
                        if (not is_safe(maze, r, c, temp)):
                            #print("INVALID SUDOKU -- > (row,col) :: ", (r, c))
                            same.append((r, c))
                        maze[r][c] = temp
            return same

        def play_Game(top, maze):
            initialize(top, maze)
            Suso(top, maze)

            if (Suso(top, maze)):
                print_maze(maze)
                alert_popup("SUCCESS ", "MAJOR ", "MISSION ACCOMPLISHED :) ")
            else:
                print("Can't find a valid solution!!!")
                alert_popup("HOUSTON WE'VE A PROBLEM :(", "Oops :( ", "Can't find a valid solution :( ")


        def createEntry(top):
            p, q = 55, 55
            for i in range(9):
                for j in range(9):
                    E = Entry(top, width=30 ,font='VarelaRound 20 ',justify='center')
                    E.place(x=p, y=q, height=40, width=40)

                    # E.pack()
                    entries.append(E)

                    p += 50
                q += 50
                p = 55

        def createRow(canvas):
            i, j = 50, 50
            p = 50
            q = 500
            for m in range(10):
                if (m % 3 == 0):
                    canvas.create_line(i, j, p, q, width=6)
                else:
                    canvas.create_line(i, j, p, q, width=1.5)
                i += 50
                p += 50

        def createCol(canvas):
            i, j = 50, 50
            p, q = 500, 50
            for m in range(10):
                if (m % 3 == 0):
                    canvas.create_line(i, j, p, q, width=5)
                else:
                    canvas.create_line(i, j, p, q, width=2.5)
                j += 50
                q += 50

        def createButtons(top, maze):
            myFont = font.Font(family='Times',size=16,weight="bold")
            button_solve = Button(top, text="SOLVE",justify='left',command=lambda: play_Game(top, maze),activeforeground = "#7fff00",activebackground = "black",font = myFont)
            button_launch = Button(top,text="LAUNCH", justify='center', command=lambda:  launch_maze(top,maze),activeforeground = "#7fff00",activebackground = "black",font = myFont)
            button_reset = Button(top, text="RESET", justify='right', command=lambda: clean_Mess(),activeforeground = "#7fff00",activebackground = "black",font = myFont)
            button_solve.place(x=50+25, y=525, height=50, width=100)
            button_reset.place(x=350+25, y=525, height=50, width=100)
            button_launch.place(x=200 +25, y=525, height=50, width=100)

        maze = self.maze

        top = Tk()
        top.geometry("550x600")
        var = StringVar()
        label = Label(top, textvariable=var)

        top.title("SuSo")

        top.configure(background='lightyellow')
        # top.configure(background = 'black')
        canvas = Canvas(top, height=600, width=550)
        canvas.configure(background='cyan')

        createRow(canvas)
        createCol(canvas)
        createEntry(top)
        createButtons(top, maze)
        canvas.pack(side='top')
        top.mainloop()


'''
maze=np.array([     [0,3,7, 0,7,2, 1,0,4],
          [0,2,0, 3,8,4, 0,6,5],
          [9,0,8, 0,0,0, 7,0,2],

          [1,8,0, 7,9,6, 0,0,3],
          [0,5,0, 2,0,1, 6,0,0],
          [6,0,0, 4,5,0, 2,1,0],

          [8,1,4, 0,0,0, 0,9,0],
          [3,6,7, 0,4,9, 5,0,0],
          [0,9,5, 0,0,3, 8,0,7]])


SUSO = UI(maze)
SUSO.createGUI()

'''





