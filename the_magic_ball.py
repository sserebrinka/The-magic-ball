from tkinter import *
import time
from random import choice
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox



#Вопросы
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

#Функция для выбора ответа
def choice_answer():
    time.sleep(0.3)
    global ans_old_1
    ans_new = ans_old_1
    while ans_new == ans_old_1:   # чтобы один и тот же ответ не выпал два раза подряд
        ans_new = choice(answers)
    ans_old_1 = ans_new
    canvas.itemconfig(answer_1, text=ans_old_1)

#Выход
def closing():
    if messagebox.askokcancel("Выход из игры", "Вы точно хотите выйти?"):
        window.destroy()


def change_the_font(event):
    text = entry.get()
    text_length = len(text)
    if text_length > 20:
        new_font_size = 18
        if text_length > 27:
            new_font_size = 15
            if text_length > 37:
                new_font_size = 10
                if text_length > 45:
                    new_font_size = 7
    else:
        new_font_size = 23

    entry.config(font=("Arial Rounded MT Bold", new_font_size))


#Создание окна
window = Tk()
window.title("The magical ball")

frame = tkinter.Frame(window)
frame.grid()

#Размер окна
window.geometry('800x750')

#Фоновое изображение
canvas = tkinter.Canvas(window, height=800, width=800)
image = Image.open("magical_ball.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=0, column=0)

#Иконка
icon = PhotoImage(file='logo.png')
window.iconphoto(False, icon)

#Кнопка выхода
our_button2 = PhotoImage(file='exit_btn_1.png')
id_button2 = Button(window, image=our_button2, highlightthickness=0,
                    bg='#B23AEE', bd=4, command=closing)
id_button2.place(x=700, y=650)


ans_old = 'Добро\nпожаловать!'
answer = canvas.create_text(410, 200, text=ans_old,
                            font=("Arial Rounded MT Bold", 25), fill='white',
                            justify=CENTER, anchor=CENTER)

ans_old_1 = 'Я знаю ответ\nна любой твой вопрос!'                              # текст с ответом
answer_1 = canvas.create_text(410, 350, text=ans_old_1,
                            font=("Arial", 20), fill='white',
                            justify=CENTER, anchor=CENTER)

#Главная кнопка
b1 = Button(window, text='ЖМИ, ЧТОБЫ УЗНАТЬ\nСВОЮ СУДЬБУ',
            font=("Arial Rounded MT Bold", 15), command=choice_answer,
            bg='#B23AEE', bd=7)
b1.place(x=250, y=480, width=330, height=60)

#Окошко для вопроса
entry = Entry(font=("Arial Rounded MT Bold", 23))
entry.place(x=250, y=430, width=330, height=40)
entry.bind("<KeyRelease>", change_the_font)


window.mainloop()