import tkinter as tk
from tkinter import messagebox
def click(event):
    global screen_text
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(screen_text.get())
            screen_text.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input!")
            screen_text.set("")
    elif text == "C":
        screen_text.set("")
    else:
        screen_text.set(screen_text.get() + text)
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0, 0)
screen_text = tk.StringVar()
screen = tk.Entry(root, textvar=screen_text, font="Arial 20 bold", bg="#f0f0f0", justify="right")
screen.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)
button_frame = tk.Frame(root)
button_frame.pack()
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]
for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(side=tk.TOP)
    for btn_text in row:
        button = tk.Button(
            button_row, text=btn_text, font="Arial 15 bold", width=5, height=2, relief="ridge"
        )
        button.pack(side=tk.LEFT, padx=2, pady=2)
        button.bind("<Button-1>", click)
root.mainloop()
