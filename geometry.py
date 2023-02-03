from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk

class Geometry(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Key Words")
        self.geometry("900x600")
        self.state("zoomed")

        self.update()
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.background_image = customtkinter.CTkImage(light_image=Image.open("pexels-adrien-olichon-2387793.jpg"), dark_image=Image.open("pexels-adrien-olichon-2387793.jpg"),
                                                       size=(self.width, self.height))

        self.picture_label=customtkinter.CTkLabel(master=self, text="", image=self.background_image)
        self.picture_label.place(x=0, y=0)


# app = Geometry()
# app.mainloop()



