from tkinter import *

chest = Tk()
chest.title("CHEST")

Image = Canvas(chest, width = 945, height = 549, bg="#000000",highlightthickness=0)      
Image.pack()
Photo = PhotoImage(file="CHEST_THUMBNAIL.png")
Image.create_image(10,5, anchor=NW, image=Photo)

chest.mainloop()