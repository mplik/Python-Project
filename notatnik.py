import tkinter as tk
from tkinter import filedialog

def save_note():
    text = entry.get("1.0", tk.END)
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

root = tk.Tk()
root.title("Super Prosty Notatnik")
entry = tk.Text(root, width=40, height=10)
entry.pack()
button = tk.Button(root, text="Zapisz notatkę", command=save_note)
button.pack()
root.mainloop()