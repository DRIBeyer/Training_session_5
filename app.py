from tkinter import *
import customtkinter
from items import Items

class App(Items):
    def __init__(self):
        super().__init__()
        self.button1.configure(command=self.filter)

    # a function within a class is called a method
    def filter(self):
        words = [self.entry_1.get(), self.entry_2.get(), self.entry_3.get(), self.entry_4.get()]
        words_filtered = [x for x in words if x != ""]
        print(words_filtered)


app = App()
app.mainloop()


