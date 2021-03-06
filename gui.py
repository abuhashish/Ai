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
        root['bg']='cyan'

        GLineEdit_209=tk.Entry(root)
        GLineEdit_209["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_209["font"] = ft
        GLineEdit_209["fg"] = "#333333"
        GLineEdit_209["justify"] = "center"
        GLineEdit_209["text"] = ""
        GLineEdit_209.place(x=60,y=120,width=224,height=30)

        GLabel_459=tk.Label(root)
       
        ft = tkFont.Font(family='Times',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["justify"] = "center"
        GLabel_459["text"] = "Welcome To Path-Finder ( AI Project)"
        GLabel_459['bg']="lightgreen"
        GLabel_459.place(x=90,y=20,width=402,height=30)

        GRadio_202=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_202["font"] = ft
        GRadio_202["fg"] = "#333333"
        GRadio_202["justify"] = "center"
        GRadio_202["text"] = "A*"
        GRadio_202.place(x=30,y=230,width=85,height=25)
        GRadio_202["command"] = self.GRadio_202_command
        GRadio_202["value"]=0
        GRadio_202["bg"]="lightgreen"

        GRadio_538=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_538["font"] = ft
        GRadio_538["fg"] = "#333333"
        GRadio_538["justify"] = "center"
        GRadio_538["text"] = "Greedy"
        GRadio_538.place(x=240,y=230,width=85,height=25)
        GRadio_538["command"] = self.GRadio_538_command
        GRadio_538["value"]=1
        GRadio_538["bg"]="lightgreen"
        
        GRadio_210=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_210["font"] = ft
        GRadio_210["fg"] = "#333333"
        GRadio_210["justify"] = "center"
        GRadio_210["text"] = "DFS"
        GRadio_210.place(x=430,y=230,width=85,height=25)
        GRadio_210["command"] = self.GRadio_210_command
        GRadio_210["value"] = 2
        GRadio_210["bg"]="lightgreen"

        GLabel_323=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_323["font"] = ft
        GLabel_323["fg"] = "#333333"
        GLabel_323["justify"] = "center"
        GLabel_323["text"] = "Please Choose The Algorithem You want to use"
        GLabel_323.place(x=50,y=190,width=283,height=30)
        GLabel_323["bg"]="lightgreen"

        GLabel_632=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_632["font"] = ft
        GLabel_632["fg"] = "#333333"
        GLabel_632["justify"] = "center"
        GLabel_632["text"] = "Please Choose Your Destination"
        GLabel_632.place(x=60,y=80,width=194,height=30)
        GLabel_632["bg"]="lightgreen"
        
        GCheckBox_235=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_235["font"] = ft
        GCheckBox_235["fg"] = "#333333"
        GCheckBox_235["justify"] = "center"
        GCheckBox_235["text"] = "Heurstics(Walk Distance)"
        GCheckBox_235.place(x=30,y=270,width=160,height=32)
        GCheckBox_235["offvalue"] = "0"
        GCheckBox_235["onvalue"] = "1"
        GCheckBox_235["command"] = self.GCheckBox_235_command
        GCheckBox_235["bg"]="lightgreen"

        GCheckBox_632=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_632["font"] = ft
        GCheckBox_632["fg"] = "#333333"
        GCheckBox_632["justify"] = "center"
        GCheckBox_632["text"] = "Heurstics(Airial Distance)"
        GCheckBox_632.place(x=30,y=300,width=160,height=30)
        GCheckBox_632["offvalue"] = "0"
        GCheckBox_632["onvalue"] = "2"
        GCheckBox_632["command"] = self.GCheckBox_632_command
        GCheckBox_632["bg"]="lightgreen"
        
        
        GButton_969=tk.Button(root)
        GButton_969["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_969["font"] = ft
        GButton_969["fg"] = "#000000"
        GButton_969["justify"] = "center"
        GButton_969["text"] = "Find"
        GButton_969.place(x=240,y=340,width=70,height=25)
        GButton_969["command"] = self.GButton_969_command
        GButton_969["bg"]="white"

        GMessage_543=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_543["font"] = ft
        GMessage_543["fg"] = "#333333"
        GMessage_543["justify"] = "center"
        GMessage_543["text"] = "Message"
        GMessage_543.place(x=20,y=390,width=551,height=100)
        GMessage_543["bg"]="lightgreen"
        


    def GRadio_202_command(self):
        print("command")


    def GRadio_538_command(self):
        print("command")


    def GRadio_210_command(self):
        print("command")


    def GCheckBox_235_command(self):
        print("command")


    def GCheckBox_632_command(self):
        print("command")
        

    def GButton_969_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
