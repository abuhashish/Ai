import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Ai Project")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='lightblue')

        GLabel_477=tk.Label(root)
        GLabel_477["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_477["font"] = ft
        GLabel_477["fg"] = "#000000"
        GLabel_477["justify"] = "center"
        GLabel_477["text"] = "Please Choose the Algorithem You want to Use"
        GLabel_477.place(x=10,y=10,width=277,height=30)

        GRadio_189=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_189["font"] = ft
        GRadio_189["fg"] = "#333333"
        GRadio_189["justify"] = "center"
        GRadio_189["text"] = "BFS"
        GRadio_189.place(x=20,y=70,width=85,height=25)
        GRadio_189["command"] = self.GRadio_189_command

        GRadio_204=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_204["font"] = ft
        GRadio_204["fg"] = "#333333"
        GRadio_204["justify"] = "center"
        GRadio_204["text"] = "Greedy"
        GRadio_204.place(x=160,y=70,width=85,height=25)
        GRadio_204["command"] = self.GRadio_204_command

        GRadio_185=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_185["font"] = ft
        GRadio_185["fg"] = "#333333"
        GRadio_185["justify"] = "center"
        GRadio_185["text"] = "A*"
        GRadio_185.place(x=300,y=70,width=85,height=25)
        GRadio_185["command"] = self.GRadio_185_command

    def GRadio_189_command(self):
        print("command")


    def GRadio_204_command(self):
        print("command")


    def GRadio_185_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
