import re #библиотека 
import csv #для таблички 
from docx import Document #для обработки файла 
import matplotlib.pyplot as plt #для гистограммы
docs = Document("lion.docx")#чтение файла
text = " ".join([para.text for para in docs.paragraphs]).lower()#выводим текст в нижний регистр
bukvi = (
    "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я "
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "à â æ ç é è ê ë î ï ô œ ù û ü ÿ"
)#считывание букв для гистограммы
list = bukvi.split()#разделяем буквы
list_counts = [text.count(ch) for ch in list]#считаем
plt.figure(figsize=(16, 6))#увеличиваем ширину графика чтобы все буквы нормально поместились 
plt.bar(list, list_counts, color='pink', edgecolor='red')#выбираем цвет 
plt.show()#выводим
yborka_list = re.findall(r"[а-яёa-zàâæçéèêëîïôœùûüÿ]+", text)#убираем все лишнее кроме букв
list_stats = {}#пустой список
for item in yborka_list:
    list_stats[item] = list_stats.get(item, 0) + 1#расчет 
with open("text.csv", "w", newline="", encoding="utf-8-sig") as out_file:
    csv_writer = csv.writer(out_file, delimiter=";")
    csv_writer.writerow(["Слово", "Частота встречи, раз", "Частота встречи в %"])#колонки
    for word_key in list_stats:
        freq_percent = round((list_stats[word_key] / len(yborka_list)) * 100, 2)
        csv_writer.writerow([word_key, list_stats[word_key], freq_percent])#пишем остальную часть таблицы

        