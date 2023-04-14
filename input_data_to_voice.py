from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=300, bg="red")
canvas.grid()


def input_data_to_text():
    text = entry_box.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save("inputtoaudio.mp3")
    os.system("start inputtoaudio.mp3")


entry_box = Entry(root)
entry_box.grid(row=0, column=0)
canvas.create_window(200, 200, window=entry_box)
button = Button(root, text="start", command=input_data_to_text)
button.grid(row=1, column=0)
canvas.create_window(200, 250, window=button)
root.mainloop()
