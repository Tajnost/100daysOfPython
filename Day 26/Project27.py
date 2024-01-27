import tkinter


window = tkinter.Tk()
window.title("Calculate deeze")
window.minsize(width=300, height=200)


def button_clicked():
    y = int(input.get())
    x = round(y * 1.609344, 2)
    print(x)
    my_label2["text"] = f"is equal to {x} km"

input = tkinter.Entry(width=5, font=("Sitka Small", 24, "bold"))
input.grid(row=0, column=1, padx=30)
input.get()

my_label = tkinter.Label(window, text=f"Miles", font=("Sitka Small", 24, "bold"))
my_label.grid(row=0, column=2)

my_label2 = tkinter.Label(window, text=f"is equal to 0 km", font=("Sitka Small", 24, "bold"))
my_label2.grid(row=1, column=1)

button = tkinter.Button(text="Calculate!", font=("Sitka Small", 24, "bold"), command=button_clicked)
button.grid(row=2, column=1)



window.mainloop()

