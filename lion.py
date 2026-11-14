import re
import csv
from docx import Document
import matplotlib.pyplot as plt

# чтение документа
docs = Document("lion.docx")
text = " ".join([para.text for para in docs.paragraphs]).lower()

# блок 1: работа с буквами (русские + французские) и построение гистограммы
bukvi = (
    "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я "
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "à â æ ç é è ê ë î ï ô œ ù û ü ÿ"
)
glist = bukvi.split()
glist_counts = [text.count(ch) for ch in glist]

# немного увеличил ширину графика, чтобы все буквы поместились без наложения
plt.figure(figsize=(16, 6))
plt.bar(glist, glist_counts, color='pink', edgecolor='red')
plt.show()

# блок 2: работа со словами (русские + французские) и сохранение в таблицу
yborka_glistov = re.findall(r"[а-яёa-zàâæçéèêëîïôœùûüÿ]+", text)
glist_stats = {}

for item in yborka_glistov:
    glist_stats[item] = glist_stats.get(item, 0) + 1

with open("text.csv", "w", newline="", encoding="utf-8-sig") as out_file:
    csv_writer = csv.writer(out_file, delimiter=";")
    csv_writer.writerow(["Слово", "Частота встречи, раз", "Частота встречи в %"])
    
    for word_key in glist_stats:
        freq_percent = round((glist_stats[word_key] / len(yborka_glistov)) * 100, 2)
        csv_writer.writerow([word_key, glist_stats[word_key], freq_percent])

        