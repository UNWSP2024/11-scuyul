#Program 1: Griffin Corniea, Qoute displayer
import tkinter as tk

saying = ('"And yet the one that comforts even the sinner is a blessed soul indeed -Griffin"')


GUI = tk.Tk()
GUI.title("MY GUI")
GUI.geometry("525x50")

label = tk.Label(GUI, text=saying)
label.pack()

GUI.mainloop()