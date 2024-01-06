#Contém a interface do usuário (UI) construída com Tkinter ou outra biblioteca gráfica. Este módulo será responsável por coletar entradas do usuário e exibir informações.

import tkinter as tk
from tkinter import messagebox
from controller import Controller

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('MindSphere Model Creator')

        self.controller = Controller(self)

        # Main layout
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Input for number of aspects
        self.lbl_num_aspects = tk.Label(self.main_frame, text="Quantos Aspects?")
        self.lbl_num_aspects.pack()

        self.entry_num_aspects = tk.Entry(self.main_frame)
        self.entry_num_aspects.pack()

        # Button to add aspects
        self.btn_add_aspects = tk.Button(self.main_frame, text="Add Aspects", command=self.add_aspects)
        self.btn_add_aspects.pack()

        # Placeholder for aspect frames
        self.aspects_frames = []

    def add_aspects(self):
        try:
            num_aspects = int(self.entry_num_aspects.get())
            self.clear_aspects()
            for _ in range(num_aspects):
                aspect_frame = AspectFrame(self.main_frame, self.controller)
                aspect_frame.pack()
                self.aspects_frames.append(aspect_frame)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of aspects")

    def clear_aspects(self):
        for aspect_frame in self.aspects_frames:
            aspect_frame.destroy()
        self.aspects_frames.clear()

    def submit(self):
        # Logic to gather all data from aspect frames and submit
        pass

class AspectFrame(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        # UI components for one aspect
        self.lbl_aspect_name = tk.Label(self, text="Aspect Name:")
        self.lbl_aspect_name.pack(side='top', fill='x')

        self.entry_aspect_name = tk.Entry(self)
        self.entry_aspect_name.pack(side='top', fill='x')

        # Placeholder for variable entries
        self.variables_frame = tk.Frame(self)
        self.variables_frame.pack()

        # Add more components as needed...

# Later, you would also define UI components for variables, asset types, etc.

if __name__ == '__main__':
    app = Application()
    app.mainloop()
