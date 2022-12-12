#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
def press(file):
    with open (file, "r",encoding='utf-8') as text:
        #with open(result,'w',encoding='utf-8') as res:
            inp_str=text.readline()
            print(inp_str)


 
press('file2.txt')

