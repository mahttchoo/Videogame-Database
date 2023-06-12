import tkinter as tk
from tkinter import Tk
from tkinter import ttk
#from tkinter import Label
from tkinter import Button
import sqlite3



# SQLite3 Setup
conn = sqlite3.connect('database.db')
cursor = conn.cursor()



# Tkinter Setup
root = Tk()
root.title("Matthew's Videogames")
#root.iconbitmap()
root.geometry("1200x500")
#root.attributes("-fullscreen", True)



# Functions!
# Searchbar text pre-fill function
def prefill(event):
    current = searchbar.get("1.0", tk.END)
    if current == "search\n":
        searchbar.delete("1.0", tk.END)
    elif current == "\n":
        searchbar.insert("1.0", "search")


def playedGames():
    print("playedGames called")
    header.configure(text="Played Games Button Clicked!") #temp


def unplayedGames():
    print("unplayedGames called")
    header.configure(text="Unplayed Games Button Clicked!") #temp


def update():
    print("update called")



# Tkinter Widgets
header = tk.Label(root, text="Matthew's Videogames!", font="Arial, 32")
header.pack(pady=50)

searchbar = tk.Text(root, height=1, width=50, font="Arial, 16")
searchbar.pack()
searchbar.insert(tk.END, "search")
searchbar.bind("<FocusIn>", prefill)
searchbar.bind("<FocusOut>", prefill)

suggestionList = tk.Listbox(root, height=5, width=67, font="Arial, 12")
suggestionList.pack()

buttonPlayedGames = tk.Button(root, text="Played Games", command=playedGames, bg="yellow")
buttonPlayedGames.pack(pady=(50, 0))

buttonUnplayedGames = tk.Button(root, text="Unplayed Games", command=unplayedGames, bg="yellow")
buttonUnplayedGames.pack()

root.mainloop()

# --- SOURCES ---
# https://youtu.be/0CXQ3bbBLVk