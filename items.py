from tkinter import *
import customtkinter
from geometry import Geometry
ENTRY_X1 = 0.1
ENTRY_X2 = 0.3
ENTRY_Y1 = 0.1
ENTRY_Y2 = 0.3

class Items(Geometry):
    def __init__(self):
        super().__init__()
        self.entry_1 = customtkinter.CTkEntry(master=self, placeholder_text="Put your key word here")
        self.entry_1.place(relx=ENTRY_X1, rely=ENTRY_Y1)
        self.entry_2 = customtkinter.CTkEntry(master=self, placeholder_text="Put your key word here")
        self.entry_2.place(relx=ENTRY_X2, rely=ENTRY_Y1)
        self.entry_3 = customtkinter.CTkEntry(master=self, placeholder_text="Put your key word here")
        self.entry_3.place(relx=ENTRY_X1, rely=ENTRY_Y2)
        self.entry_4 = customtkinter.CTkEntry(master=self, placeholder_text="Put your key word here")
        self.entry_4.place(relx=ENTRY_X2, rely=ENTRY_Y2)

        self.button1= customtkinter.CTkButton



app = Items()
app.mainloop()

