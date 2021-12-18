import tkinter as tk
from tkinter import filedialog, Text
import os


# the app "body"
root = tk.Tk()


def addApp():
    filename = filedialog.askopenfilename(initaldir="/", title="Select File",
                                            filetypes=(("executables", "*.exe"),
                                            ("all files", "*.*")))


#Create canvas
canvas = tk.Canvas(root, height=900, width=900, bg="#263D42")
canvas.pack

# attach things to root
frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

chooseApps = tk.Button(root, text="Add App", padx=10, pady=5,
                        bg="#263D42" "command"=addApp)
chooseApps.pack()


runApps = tk.Button(root, text="Add App", padx = 10, pady=5, bg="#263D42")
runApps.pack()


root.mainloop()
