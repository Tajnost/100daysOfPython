from tkinter import *
import pandas
import random
from time import sleep
BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("./data/learn_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

test = data.to_dict('records')
randomy ={}

def randomWord():
    window.update()
    global randomy,timerflip
    window.after_cancel(timerflip)
    randomy = random.choice(test)
    canvas.itemconfig(card_background, image=logo_img)
    canvas.itemconfig(translation_text, text="French", fill="black")
    canvas.itemconfig(translation_word, text=randomy["French"], fill="black")
    timerflip = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(translation_text, text="English", fill="white")
    canvas.itemconfig(translation_word, text=randomy["English"], fill="white")
    canvas.itemconfig(card_background, image=logo_img2)
    window.update()

def remove():
    test.remove(randomy)
    print(len(test))
    randomWord()
    data = pandas.DataFrame(test)
    data.to_csv("./data/learn_words.csv")

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timerflip = window.after(3000, func=flip_card)



#Canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="./images/card_front.png")
logo_img2 = PhotoImage(file="./images/card_back.png")
card_background= canvas.create_image(410,268, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Words
translation_text = canvas.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, "bold"))
translation_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

#Buttons
my_image1 = PhotoImage(file="./images/right.png")
rightButton = Button(image=my_image1, highlightthickness=0, command=randomWord)
rightButton.grid(row=2, column=1)

my_image2 = PhotoImage(file="./images/wrong.png")
wrongButton = Button(image=my_image2, highlightthickness=0, command=remove)
wrongButton.grid(row=2, column=0)






randomWord()


window.mainloop()