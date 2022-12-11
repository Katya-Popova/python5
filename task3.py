#Создайте программу для игры в ""Крестики-нолики"".
l=[1,2,3,4,5,6,7,8,9]
x=0
print(l[:3],l[3:6],l[6:], sep="\n")

def ogame(x,l):
    print("\nВведите номер ячейки для хода")
    x=int(input())
    l[x-1]=0
    print(l[:3],l[3:6],l[6:], sep="\n")

def xgame(x,l):
    print("\nВведите номер ячейки для хода")
    x=int(input())
    l[x-1]='X'
    print(l[:3],l[3:6],l[6:], sep="\n")

def pobeda(l):
    if (l[0]==l[1]  and l[0]==l[2]) or (l[0]==l[3] and l[0]==l[6]) or (l[0]==l[4] and l[0]==l[8]) or (l[1]==l[4] and l[4]==l[7]) or (l[2]==l[5] and l[5]==l[8]) or (l[2]==l[4] and l[4]==l[6]):
        print('\nПобеда')


while x<=len(l):
    xgame(x,l)
    if (l[0]==l[1]  and l[0]==l[2]) or (l[0]==l[3] and l[0]==l[6]) or (l[0]==l[4] and l[0]==l[8]) or (l[1]==l[4] and l[4]==l[7]) or (l[2]==l[5] and l[5]==l[8]) or (l[2]==l[4] and l[4]==l[6]):
        print('\nПобедили Х')
        break
    ogame(x,l)
    if (l[0]==l[1]  and l[0]==l[2]) or (l[0]==l[3] and l[0]==l[6]) or (l[0]==l[4] and l[0]==l[8]) or (l[1]==l[4] and l[4]==l[7]) or (l[2]==l[5] and l[5]==l[8]) or (l[2]==l[4] and l[4]==l[6]):
        print('\nПобедили О')
        break

