#Program 2: Griffin Corniea, Info getter
import tkinter as tk

def show_info():
    info_label.config(text="Name: Griffin Corniea\nAddress: 123 Example Street\nCity: Springfield, USA")

def quit_app():
    GUI.destroy()

GUI = tk.Tk()
GUI.title("User Info")
GUI.geometry("300x200")

info_label = tk.Label(GUI, text="", justify="left", font=("Arial", 12))
info_label.pack(pady=20)

show_button = tk.Button(GUI, text="Show Info", command=show_info, width=12)
show_button.pack(pady=5)

quit_button = tk.Button(GUI, text="Quit", command=quit_app, width=12)
quit_button.pack(pady=5)

GUI.mainloop()
