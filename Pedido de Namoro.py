import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Pedido de Namoro')
root.geometry('600x600')
root.configure(background='#212121')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 50:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Meu amor', 'Eu te amo meu amor <3')

def denied():
    button_1.destroy()

margin = Canvas(root, width=500, bg='#212121', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg='#212121', text='Quer namorar comigo?', fg='#FF4081', font=('Times New Roman', 25, 'bold'))
text_id.pack()

font_style = tkfont.Font(family="Arial", size=12, weight="bold")

button_1 = tk.Button(root, text='Não', bg='#FF4081', fg='white', activebackground='#FF69B4', activeforeground='white',
                     command=denied, relief=FLAT, bd=0, font=font_style)
button_1.pack(pady=20)

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#FF4081', fg='white', activebackground='#FF69B4', activeforeground='white',
                     relief=FLAT, bd=0, command=accepted, font=font_style)
button_2.pack()

root.mainloop()