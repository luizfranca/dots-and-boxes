from Tkinter import Tk, Canvas, Frame, BOTH
import sys

class BoardUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

    def initUI(self, n, m, table = []):
        self.parent.title("Dots and Boxes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        if (len(table) == 0):
            self.initUIFilled(n, m, canvas)
        else:
            self.initUIWithTable(n, m, canvas, table)

        canvas.pack(fill=BOTH, expand=1)

    def initUIWithTable(self, n, m, canvas,table):

        for i in range(n):
            for j in range(m):
                
                # create dots
                canvas.create_oval(10 + j * 45, 10 + i * 45, 20 + j * 45, 20 + i * 45, fill='blue')

        isHorizontal = True
        i = 0
        for line in table:
            j = 0
            for item in list(line):

                if (item == "_" or item == "X"):
                    if (item == "X"):
                        if (isHorizontal):
                            canvas.create_line(25 + j * 45, 15 + i * 45, 50 + j * 45, 15 + i * 45, width=3, fill="red")
                        else:
                            canvas.create_line(15 + j * 45, 25 + i * 45, 15 + j * 45, 50 + i * 45, width=3, fill="red")

                    j+=1
                elif (item == "B" or item == "W"):
                    color = "black" if item == "B" else "white"
                    canvas.create_rectangle(20 + (j - 1) * 45, 20 + i * 45, 55 + (j - 1) * 45, 55 + i * 45, fill=color, width = 2)

            isHorizontal = not isHorizontal
            if ("B" in line or "W" in line or "*" in line):
                i += 1

    def initUIFilled(self, n, m, canvas):
        for i in range(n):
            for j in range(m):
                canvas.create_oval(10 + j * 45, 10 + i * 45, 20 + j * 45, 20 + i * 45, fill='blue')

def main(n, m, table = []):
    root = Tk()

    ex = BoardUI(root)
    ex.initUI(n, m, table)
    x, y = m * 45 - 10, n * 45 - 10

    root.geometry(str(x) + "x" + str(y) + "+0+0")
    root.mainloop()

if __name__ == "__main__":
    args = sys.argv[1:]
    table = []

    if (len(args) < 2):
        m = args[0].split("|")[0].count(".")
        n = args[0].count(".") / m
        table = args[0].upper().replace(".", "").split("|")
    else:
        n = int(args[0])
        m = int(args[1])
    main(n, m, table)