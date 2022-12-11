file = 'Аты-абваты, шли солдабвты, Абвты-бабвты, на бабвзар. Абвты-бабвты, что купили? Аты-бабвты, сабвмовар. Аты-бабвты, сколько стоит? Аты-бабвты, три рубля. Аты-баты, он какой? Аты-баты, золотой.'
def delete_words(file):
    file=list(filter(lambda x: 'абв' not in x, file.split()))
    return " ".join(file)
file=delete_words(file)
print(file)

import random

player1=input('Введите имя первого игрока ')
player2=input('Введите имя второго игрока ')
candys1=0
candys2=0
AllCandys=2021
change=random.randrange(1,2)
if change==1:
    print('Первым ходит ', player1)
else:
    print('Ходит игрок ', player2)
while AllCandys>0:
    if AllCandys>28:
        candys1=int(input('Возьми не более 28 конфет '))
        AllCandys=AllCandys-candys1
        print('Осталось ', AllCandys,' конфет')
        if AllCandys>28:
            candys2=int(input('Возьми не более 28 конфет '))
            AllCandys=AllCandys-candys2
            print('Осталось ', AllCandys,' конфет')
            if AllCandys<=28:
                if change==1:
                    print('Оставшиеся', AllCandys, 'конфет отдаются', player1,'. Победил ', player1)
                else: print('Оставшиеся', AllCandys, 'конфет отдаются', player2,'. Победил ', player2)
        else:
            if change==1:
                print('Оставшиеся', AllCandys, 'конфет отдаются', player2,'. Победил ', player2)
            else: print('Оставшиеся', AllCandys, 'конфет отдаются', player1,'. Победил ', player1)

from tkinter import *
import random

root=Tk()
root.title('Крестики нолики')
root.geometry('350x350')

games=Canvas(root, width=300, height=300, bg='#CCCCCC')
games.place(x=25, y=25)

condition=[None]*9
win=None
combinations=[(0,1,2),(3,4,6),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

for i in range(0,9):
    x=i//3*100
    y=1%3*100
    games.create_rectangle(x,y,x+100,y+100,
                        width=3,
                        outline='#A5A5A5',
                        fill='#CCCCCC',
                        activefill='#FFFAFA')

def winner():
    global win
    variants=[]
    for i in combinations:
        variants.append([condition[i[0]],condition[i[1]],condition[i[2]]])
    if ['x']*3 in variants:
        win='Выйграл игрок.'
    elif ['0']*3 in variants:
        win='Бот выйграл.'
    elif None not in condition:
        win='Ничья.'
    return win

def end_game():
    print(f'Игра окончена {win}')

def add_x(colum,row):
    x=10+100*colum
    y=10+100*row
    games.create_line(x,y,x+80,y+80, width=7, fill='#0000FF')
    games.create_line(x,y+80,x+80,y, width=7, fill='#0000FF')

def add_0(colum, row):
    x=10+100*colum
    y=10+100*row
    games.create_oval(x,y,x+80,y+80,width=7,outline='#FF0000')

def click(event):
    colum=event.x//100
    row=event.y//100
    index=colum+row*3
    if condition[index] is None:
        condition[index]='x'
        add_x(colum,row)
        if winner():
            end_game()
        else:
            bot_move()
            if winner():
                end_game
    bot_move()
    print(condition)

def bot_move():
    empty_indexes=[]
    for index, el in enumerate(condition):
        if el is None:
            empty_indexes.append(index)
    index=random.choice(empty_indexes)
    condition[index]='0'
    colum=index%3
    row=index//3
    add_0(colum,row)

games.bind('<Button-1>', click)

root.mainloop()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")