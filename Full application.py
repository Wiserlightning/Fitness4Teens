import tkinter as tk

heltitle = ("Helvetica", 20, "bold")

class Fitness4Teens(tk.TK):

    def __init__(slef, *args, **kwargs):

        tk.TK.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill'both', expand = True)

        container.grid_rowconfigure(0, weight = 1)

        container.grid_coumnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(slef, parent)
        label = tk.Label(self,text="Fitness4Teens", font=heltitle)
        label.pack(pady=10, padx=10)

app = Fitness4Teens()
app.mainloop
#I will create a bunch of application functions seperately and then merge them all into this file