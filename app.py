import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "r") as file:
        content = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, content)
        showinfo("Opened", f"Opened file: {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as file:
        file.write(text.get(1.0, tk.END))
        showinfo("Saved", f"Saved to: {filepath}")

# Main Window
root = tk.Tk()
root.title("Text Editor in Python")
root.geometry("700x500")

# Menu
menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Edit")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="File", menu=file_menu)
root.config(menu=menu)

# Text Area
text = tk.Text(root, wrap=tk.WORD, font=("Arial", 14))
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()
