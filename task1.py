#Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text=" hbvj, впиишр, укп, купипк, абв, аваыц"
text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text.split()))
print(text_list)