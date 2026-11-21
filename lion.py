import csv 
from collections import Counter 
import docx
import matplotlib.pyplot as plt
doc=docx.Document('lion.docx')#читаем файл
text=''#пустая стока для сбора всего текста
for a in doc.paragraphs:
    text=text+' '+a.text#собираем текст
text=text.lower()#переводим в нижний регистр
znaki = '.,!?;:"()«»—–-'#задаем знаки чтобы потом если встречать их в тексте то менять на пробелы 
for i in znaki:
    text = text.replace(i, ' ')
slova=text.split()#разбиваем слова для посчета 
vsego_slov = len(slova)
schet_slov = Counter(slova)#считаем слова 
with open('slova.csv', 'w', encoding='utf-8-sig', newline='') as s:#создаем цсв для таблички 
    writer = csv.writer(s, delimiter=';')#задаем ; чтобы данные таблички попадали в разные столбцы
    writer.writerow(['Слово', 'Частота встречи, раз', 'Частота встречи в %'])#шапка таблицы в строчку 
    for slova, count in schet_slov.most_common():#таблт будет идти от самых частых слов к самым редким
        percent = round((count / vsego_slov) * 100, 2)#считаем встречаемость в процентах и округляем до сотых
        writer.writerow([slova, count, percent])#записывает новое слово в новую стоку
vsego_bukv=[]#список для подсчета букв
for bukvi in text:
    if bukvi.isalpha():#поверяет это буква из алфавита или знак
        vsego_bukv.append(bukvi)#если буква то добавляет
letter_counts = Counter(vsego_bukv)#считаем сколько букв
sorted_letters=sorted(letter_counts.items())#сортируем их
x_bukvi=[]#список для осей гистограммы
y_kolichestvobukv=[]#список для осей гистограммы
for item in sorted_letters:
    x_bukvi.append(item[0])#добавляет букву
    y_kolichestvobukv.append(item[1])#добавляет количество
plt.figure(figsize=(10, 5))#размер гистограммы
plt.bar(x_bukvi, y_kolichestvobukv, color='red', edgecolor='green')#оформление
plt.title('Встречаемость букв в тексте')#шапка
plt.xlabel('Буквы')#название осей 
plt.ylabel('Количество')#название осей 
plt.grid(axis='y', linestyle='--')#рисует вертикальные прямые для гистограммы
plt.show()#вывод гистограммы


        