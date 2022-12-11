# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random

n=100
men=random.randint(1,6)
comp=random.randint(1,6)
name=0
def lot(x,y,name):
     if x<y:
         name='компьютер'
         return name
     elif x>=y:
         name="игрок"
         return name
    
      
print(f'Первым ходит тот у кого выпало болшее число. Первое число ваш ход,второе ход компьютераю Если числа равные, то ваш ход.{men},{comp}')
print(f"Первым ходит: {lot(men,comp,name)}")

    
x=0
y=random.randint(1,28)
count=n
if lot(men,comp,name)=="игрок":
    while n>0:
        x=int(input())
        count=n-x
        print(f"{n}-{x}={count}")
        if count<29:
            print("Выиграл компьютер)")
            break
        n=count-y
        print(f"{count}-{y}={n}")
        if n<29:
            print("Выиграли вы)")
            break
else:
    while n>0:
        n=count-y
        print(f"{n}={count}-{y}")
        if n<29:
            print("Выиграли вы)")
            break   
        x=int(input())
        count=n-x
        print(f"{count}={n}-{x}")
        if count<29:
            print("Выиграл компьютер)")
            break
 
