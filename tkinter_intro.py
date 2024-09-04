import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# background image using label 
# PhotoImage supports GIF, PGM, PPM, and PNG file formats
# ** pillow library can do the conversion to other formats like jpg.
bg = tkinter.PhotoImage(file = "images/background.png") 
label1 = tkinter.Label( window, image = bg) 
label1.place(x = 0, y = 0) 


# label
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()


def button_got_clicked():
    # label["text"] = "Button Got Clicked"
    label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_got_clicked)
button.pack()

entry = tkinter.Entry(width=10)
entry.pack()

window.mainloop()
