import tkinter as tk
from tkinter import Tk
import sqlite3

import titlepage
import viewsinglegame
import viewgamelist
import addgame
import editgame



# SQLite3 Setup
conn = sqlite3.connect('database.db')
cursor = conn.cursor()



# Tkinter Setup
root = Tk()
root.title("Matthew's Videogames")
#root.iconbitmap()
root.geometry("1200x500")
#root.attributes("-fullscreen", True)



# Tkinter Frame Setup
titlePageFrame = tk.Frame(root)
addGameFrame = tk.Frame(root)
viewSingleGameFrame = tk.Frame(root)
viewGameListFrame = tk.Frame(root)



# Functions!
# Searchbar text pre-fill function
def prefill(event):
    current = searchbar.get("1.0", tk.END)
    if current == "search\n":
        searchbar.delete("1.0", tk.END)
    elif current == "\n":
        searchbar.insert("1.0", "search")

def playedGames():
    titlePageFrame.pack_forget()
    addGameFrame.pack()

def unplayedGames():
    addGameFrame.pack_forget()
    titlePageFrame.pack()

def update():
    print("update called")



# Title Page Frame Widgets
header = tk.Label(titlePageFrame, text="Matthew's Videogames!", font="Arial, 32")
header.pack(pady=50)

searchbar = tk.Text(titlePageFrame, height=1, width=50, font="Arial, 16")
searchbar.pack()
searchbar.insert(tk.END, "search")
searchbar.bind("<FocusIn>", prefill)
searchbar.bind("<FocusOut>", prefill)

suggestionList = tk.Listbox(titlePageFrame, height=5, width=67, font="Arial, 12")
suggestionList.pack()

buttonPlayedGames = tk.Button(titlePageFrame, text="Next Page", command=playedGames, bg="yellow")
buttonPlayedGames.pack(pady=(50, 0))

#buttonUnplayedGames = tk.Button(titlePageFrame, text="Unplayed Games", command=unplayedGames, bg="yellow")
#buttonUnplayedGames.pack()



# Add Game Frame Widgets
label = tk.Label(addGameFrame, text="test")
label.pack()

buttonUnplayedGames = tk.Button(addGameFrame, text="Back", command=unplayedGames, bg="yellow")
buttonUnplayedGames.pack()



# Running the Actual Stuff
titlePageFrame.pack()
root.mainloop()

# --- SOURCES ---
# https://youtu.be/0CXQ3bbBLVk
# https://youtu.be/95tJO7XJlko