import tkinter


window = tkinter.Tk()
window.title("MY First Tkinter Program")
window.minsize(width=800, height=600)

def button_clicked():
    my_label["text"] = input.get()


## Label

my_label = tkinter.Label(window, text="I am a label", font=("Sitka Small", 24, "bold"))
my_label.place(x=0, y=0)

#### Button



button = tkinter.Button(text="Click me!", font=("Sitka Small", 24, "bold"), command=button_clicked)
button.place(x=0, y=50)

### Entry

input = tkinter.Entry()
input.place(x=0, y=100)
input.get()



window.mainloop()



