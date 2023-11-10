'''
This is a simple application that shows the name 'Aba', a number 0, and two buttons.
Every time the "Increment" button is clicked, the number is increased by 1.
The "Restart" button resets the number to 0.
'''
import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Incrementer")
        self.geometry("200x100")
        self.number = 0
        self.label = tk.Label(self, text="Aba")
        self.label.pack()
        self.number_label = tk.Label(self, text=str(self.number))
        self.number_label.pack()
        self.button = tk.Button(self, text="Increment", command=self.increment_number)
        self.button.pack()
        self.restart_button = tk.Button(self, text="Restart", command=self.restart_count)
        self.restart_button.pack()
    def increment_number(self):
        self.number += 1
        self.number_label.config(text=str(self.number))
    def restart_count(self):
        self.number = 0
        self.number_label.config(text=str(self.number))
if __name__ == "__main__":
    app = Application()
    app.mainloop()