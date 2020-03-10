from tkinter import *
#Welcome to my app, if you want to add anything to this new GUI to give back to community feel free to
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Fitness4You") #Title

        self.pack(fill = BOTH, expand = 1) #You can resize window and it fills the window

        #create quit button 

        #creating the physical button
        
        quitButton = Button(self, text = "Quit")

        quitButton.place(x=0, y=0)

        #programming what the button does

#Calling the root window
root = Tk()
root.geometry("1200x628")

app = Window(root)

#Run the main loop
root.mainloop()