from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import time
import random

tk = Tk()  # Создаём окно
tk.title('Апит содок')  # Заголовок окна
board = Canvas(tk, width=795, height=795, bg='#FFFFFF')
tk.resizable(width=False, height=False)
board.pack()
app_running = True
tk.update()

hod_igroka = True
vozmozhnost_shodit = False
blue_count = 16
yellow_count = 16


def izobrazheniya_figur():  # загружаем изображения фигур
    global figuri
    i1 = PhotoImage(file="res\\blue.png")
    i2 = PhotoImage(file="res\\yellow.png")
    figuri = [0, i1, i2]


def novaya_igra():  # начинаем новую игру
    global pole

    pole = [[2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1]]


def Start_new():
    global blue_count
    global yellow_count
    global hod_igroka
    if askyesno("Игра закончена", "Хотите начать новую?"):
        novaya_igra()
        vivod(-1, -1)
        hod_igroka = True
        blue_count = 16
        yellow_count = 16


def vivod(x_poz_1, y_poz_1):  # рисуем игровое поле
    global figuri
    global pole

    k = 100
    x = 0
    board.delete('all')
    while x < 8 * k:  # рисуем доску
        y = k
        while y < 8 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="White")
            y += k
        x += k
    x = 0
    while x < 8 * k:  # рисуем доску
        y = 0
        while y < 8 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="White")
            y += k
        x += k

    for y in range(8):  # рисуем стоячие пешки
        for x in range(8):
            z = pole[y][x]
            if z:
                if (x_poz_1, y_poz_1) != (x, y):  # стоячие пешки?
                    board.create_image(x * k, y * k, anchor=NW, image=figuri[z])


def vozmozhnost_hodit(x, y):  # метод, проверяющий шашки на доступность хода(что им ничего не преграждает путь)
    global vozmozhnost_shodit
    global prev_coord_x
    global prev_coord_y

    if pole[x][y] != 0:  # если нажали на шашку
        if (x > 0 and pole[x - 1][y] == 0) or (pole[x + 1][y] == 0 and x < 7) or (y < 7 and pole[x][y + 1] == 0) or (
                pole[x][y - 1] == 0 and y > 0):
            vozmozhnost_shodit = True
        else:
            vozmozhnost_shodit = False
        prev_coord_x = x
        prev_coord_y = y

def click_event(event):
    global hod_igroka
    global blue_count
    global yellow_count
    global vozmozhnost_shodit
    global prev_coord_x
    global prev_coord_y

    def blue_check():
        global hod_igroka
        global yellow_count
        if y > 0 and y < 7 and pole[x][y - 1] == 2 and pole[x][y + 1] == 2:
            pole[x][y - 1] = 0
            pole[x][y + 1] = 0
            yellow_count -= 2
            vivod(-1, -1)
        elif x > 0 and x < 7 and pole[x - 1][y] == 2 and pole[x + 1][y] == 2:
            pole[x - 1][y] = 0
            pole[x + 1][y] = 0
            yellow_count -= 2
            vivod(-1, -1)
        elif y < 6 and pole[x][y + 1] == 2 and pole[x][y + 2] == 1:
            pole[x][y + 1] = 0
            yellow_count -= 1
            vivod(-1, -1)
        elif y > 1 and pole[x][y - 1] == 2 and pole[x][y - 2] == 1:
            pole[x][y - 1] = 0
            yellow_count -= 1
            vivod(-1, -1)
        elif x < 6 and pole[x + 1][y] == 2 and pole[x + 2][y] == 1:
            pole[x + 1][y] = 0
            yellow_count -= 1
            vivod(-1, -1)
        elif x > 1 and pole[x - 1][y] == 2 and pole[x - 2][y] == 1:
            pole[x - 1][y] = 0
            yellow_count -= 1
            vivod(-1, -1)
        if yellow_count == 0:
            messagebox.showinfo(title='Победа синих', message='Победили синие.', icon='info')
            hod_igroka = None
            Start_new()
    def yellow_check():
        global hod_igroka
        global blue_count
        if y > 0 and y < 7 and pole[x][y - 1] == 1 and pole[x][y + 1] == 1:
            pole[x][y - 1] = 0
            pole[x][y + 1] = 0
            blue_count -= 2
            vivod(-1, -1)
        elif x > 0 and x < 7 and pole[x - 1][y] == 1 and pole[x + 1][y] == 1:
            pole[x - 1][y] = 0
            pole[x + 1][y] = 0
            blue_count -= 2
            vivod(-1, -1)
        elif y < 6 and pole[x][y + 1] == 1 and pole[x][y + 2] == 2:
            pole[x][y + 1] = 0
            blue_count -= 1
            vivod(-1, -1)
        elif y > 1 and pole[x][y - 1] == 1 and pole[x][y - 2] == 2:
            pole[x][y - 1] = 0
            blue_count -= 1
            vivod(-1, -1)
        elif x < 6 and pole[x + 1][y] == 1 and pole[x + 2][y] == 2:
            pole[x + 1][y] = 0
            blue_count -= 1
            vivod(-1, -1)
        elif x > 1 and pole[x - 1][y] == 1 and pole[x - 2][y] == 2:
            pole[x - 1][y] = 0
            blue_count -= 1
            vivod(-1, -1)
        if blue_count == 0:
            messagebox.showinfo(title='Победа жёлтых', message='Победили жёлтые.', icon='info')
            hod_igroka = None
            Start_new()
    if 0 < event.x < 800 and 0 < event.y < 800:  # Если кликнули на доске
        x = event.y // 100  # Определяем строку на которую нажали
        y = event.x // 100  # Определяем столбец на который нажали

    if hod_igroka:
        vozmozhnost_hodit(x, y)
        if vozmozhnost_shodit:
            if pole[prev_coord_x][prev_coord_y] == 1 and pole[x][y] == 0:
                if prev_coord_x > x and prev_coord_y == y:
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_coord_x
                    for k in range(prev_coord_x, x, -1):  # проверка на пустой путь до выбранной клетки
                        ch_count += 1
                        if pole[prev_coord_x][y] != 0:
                            not_zero_count += 1
                        prev_coord_x -= 1
                    if not_zero_count == 1:  # если ничего не преграждает путь
                        pole[x][y] = 1
                        pole[prev_x][prev_coord_y] = 0
                        hod_igroka = False
                        blue_check()
                        vivod(-1, -1)
                if prev_coord_x < x and prev_coord_y == y:
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_coord_x
                    for k in range(prev_coord_x, x):
                        ch_count += 1
                        if pole[prev_coord_x][y] != 0:
                            not_zero_count += 1
                        prev_coord_x += 1
                    if not_zero_count == 1:
                        pole[x][y] = 1
                        pole[prev_x][prev_coord_y] = 0
                        hod_igroka = False
                        blue_check()
                        vivod(-1, -1)
                if prev_coord_y > y and prev_coord_x == x:
                    ch_count = 0
                    not_zero_count = 0
                    prev_y = prev_coord_y
                    for k in range(prev_coord_y, y, -1):
                        ch_count += 1
                        if pole[x][prev_coord_y] != 0:
                            not_zero_count += 1
                        prev_coord_y -= 1
                    if not_zero_count == 1:
                        pole[x][y] = 1
                        pole[prev_coord_x][prev_y] = 0
                        hod_igroka = False
                        blue_check()
                        vivod(-1, -1)
                if prev_coord_y < y and prev_coord_x == x:
                    ch_count = 0
                    not_zero_count = 0
                    prev_y = prev_coord_y
                    for k in range(prev_coord_y, y):
                        ch_count += 1
                        if pole[x][prev_coord_y] != 0:
                            not_zero_count += 1
                        prev_coord_y += 1
                    if not_zero_count == 1:
                        pole[x][y] = 1
                        pole[prev_coord_x][prev_y] = 0
                        hod_igroka = False
                        blue_check()
                        vivod(-1, -1)

    if hod_igroka == False:
        vozmozhnost_hodit(x, y)
        if vozmozhnost_shodit:
            if pole[prev_coord_x][prev_coord_y] == 2 and pole[x][y] == 0:
                if prev_coord_x > x and prev_coord_y == y:
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_coord_x
                    for k in range(prev_coord_x, x, -1):  # проверка на пустой путь до выбранной клетки
                        ch_count += 1
                        if pole[prev_coord_x][y] != 0:
                            not_zero_count += 1
                        prev_coord_x -= 1
                    if not_zero_count == 1:  # если ничего не преграждает путь
                        pole[x][y] = 2
                        pole[prev_x][prev_coord_y] = 0
                        hod_igroka = True
                        yellow_check()
                        vivod(-1, -1)
                if prev_coord_x < x and prev_coord_y == y:
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_coord_x
                    for k in range(prev_coord_x, x):
                        ch_count += 1
                        if pole[prev_coord_x][y] != 0:
                            not_zero_count += 1
                        prev_coord_x += 1
                    if not_zero_count == 1:
                        pole[x][y] = 2
                        pole[prev_x][prev_coord_y] = 0
                        hod_igroka = True
                        yellow_check()
                        vivod(-1, -1)
                if prev_coord_y > y and prev_coord_x == x:
                    ch_count = 0
                    not_zero_count = 0
                    prev_y = prev_coord_y
                    for k in range(prev_coord_y, y, -1):
                        ch_count += 1
                        if pole[x][prev_coord_y] != 0:
                            not_zero_count += 1
                        prev_coord_y -= 1
                    if not_zero_count == 1:
                        pole[x][y] = 2
                        pole[prev_coord_x][prev_y] = 0
                        hod_igroka = True
                        yellow_check()
                        vivod(-1, -1)
                if prev_coord_y < y and prev_coord_x == x:
                    ch_count = 0
                    not_zero_count = 0
                    prev_y = prev_coord_y
                    for k in range(prev_coord_y, y):
                        ch_count += 1
                        if pole[x][prev_coord_y] != 0:
                            not_zero_count += 1
                        prev_coord_y += 1
                    if not_zero_count == 1:
                        pole[x][y] = 2
                        pole[prev_coord_x][prev_y] = 0
                        hod_igroka = True
                        yellow_check()
                        vivod(-1, -1)

izobrazheniya_figur()  # здесь загружаем изображения пешек
novaya_igra()  # начинаем новую игру
vivod(-1, -1)  # рисуем игровое поле
board.bind("<Button-1>", click_event)  # нажатие левой кнопки

mainloop()
