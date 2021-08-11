from tkinter import *
from datetime import date
from PIL import ImageTk, Image

root = Tk()
root.title("Times of Ghatotkach")
root.geometry("1200x2000")
label_title = Label(text="Times of Ghatotkach", bg='Moccasin', font=("Arial", 20, "bold"), padx= 34, pady= 13)
label_title.pack(fill=X)

# label date
label_date = Label(text=f"{date.today}, Kolkata", font=("Times", 10, "bold"), padx=12, pady=7, borderwidth=3, relief=RIDGE)
label_date.pack(anchor="nw")

label_description = Label(text=f"A mentor is a person or friend who guides a less experienced person by building trust \n and modeling positive behaviors.\n An effective mentor understands that his or her role is to be dependable, \nengaged, authentic, and tuned into the needs of the mentee.\n ", bg="grey", font=("Times", 12, "bold italic"), padx=34, pady= 13)
label_description.pack(fill=X)

img = Image.open("goodmentor.jpg")
width, height = img.size
print(width)
print(height)

img = img.resize((round(290/height*width), round(300)))
img = ImageTk.PhotoImage(img)
label_image = Label(image=img)
label_image.pack(anchor="nw")
print(img.height())
print(img.width())

label_para1 = Label(text= f"Today, most youth development organizations recognise the importance of a child having a caring responsible adult in their lives.\nFor children who coma from less than ideal circumstances, mentoring can be a critical ingredient towards positive youth outcomes.\nDevelopmental psychologist and co-founder of Head Start, Urie Bronfenbrenner said it best,\na development, it turns out, occurs through this process of progressively more complext exchange between\na child and somebody else specially somebody who's crazy about that child\n", bg="black", fg='white', font=('Helvetica', 12), padx= 34, pady= 13)
label_para1.pack(fill=X)

label_para1 = Label(text = "Get ready to be the part of mentornext family.",bg = 'lightgrey', fg = 'black' ,font = ("Helvetica", 12), padx = 34, pady = 13)
label_para1.pack(fill = X,side = BOTTOM)

root.mainloop()