from Tkinter import *
import tkMessageBox
import random
secret = random.randint(0,100)
print secret
window = Tk()

# greeting text
greeting = Label(window, text="Guess the secret number")
greeting.pack()

eingabefeld = Entry(window)
eingabefeld.pack()


def geklicked():
    try:
        eingabe = int(eingabefeld.get())
    except ValueError:
        return
    if eingabe == secret:
        tkMessageBox.showinfo("nice", "Yeyyy, you guessed it.\n\nThe secret number is " + str(secret))
    else:
        tkMessageBox.showerror("damn", "not good")
    #print "klick"


knopf = Button(window, text="Send", command=geklicked)
knopf.pack()




window.mainloop()
