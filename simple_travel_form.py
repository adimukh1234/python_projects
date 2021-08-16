from tkinter import *

def getvals():
    print("It works")
root = Tk()

root.geometry("655x344")
Label(root, text="Welcome to Aditya Travels", font="helvetica").grid(row=0, column= 5)

# text in form
name = Label(root, text="Name")
gender = Label(root, text="Gender")
phn = Label(root, text="Phone Number")
emergency = Label(root, text="Emergency Number")
payment = Label(root, text="Payment Mode")

# packing text
name.grid(row= 1, column=3)
gender.grid(row= 2, column=3)
phn.grid(row= 3, column=3)
emergency.grid(row= 4, column=3)
payment.grid(row= 5, column=3)

# making variable
namevalue = StringVar()
gendervalue = StringVar()
phonevalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()


# making entry
nameentry = Entry(root, textvariable=namevalue)
genderentry = Entry(root, textvariable=gendervalue)
phoneentry = Entry(root, textvariable=phonevalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# packing entry
nameentry.grid(row=1, column=5)
genderentry.grid(row=2, column=5)
phoneentry.grid(row=3, column=5)
emergencyentry.grid(row=4, column=5)
paymententry.grid(row=5, column=5)


# checkbox+ packing
foodservice = Checkbutton(root, text="Want to prebook meals?", variable=foodservicevalue).grid(row=6, column=5)

# making button
Button(root, text="Submit Form", font="comicsanms 25 bold", command=getvals).grid(row=8, column=5)


root.mainloop()