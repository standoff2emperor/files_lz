import pandas as pd
import matplotlib.pyplot as plt

# 1. Конвертация исходных данных и чтение таблицы
raw_data = pd.read_parquet("titanic.parquet")
raw_data.to_csv("output.csv", index=False, encoding="utf-8")

passengers = pd.read_csv("output.csv")

# 2. Группировка и расчет долей в процентах (через groupby вместо crosstab)
stats = passengers.groupby(["Pclass", "Survived"]).size().unstack(fill_value=0)
percentages = stats.div(stats.sum(axis=1), axis=0) * 100

# 3. Подготовка данных и визуализация
class_labels = ["Первый класс", "Второй класс", "Третий класс"]
alive_share = percentages[1].values
dead_share = percentages[0].values

plt.figure(figsize=(9, 6))

# Отрисовка столбцов с измененными цветами и шириной
plt.bar(class_labels, alive_share, width=0.55, color="#2E8B57", edgecolor="black", label="Выжившие")
plt.bar(class_labels, dead_share, width=0.55, bottom=alive_share, color="#CD5C5C", edgecolor="black", label="Погибшие")

# Настройка оформления графика
plt.title("Доля выживших и погибших пассажиров по классам (%)", fontsize=13, pad=12)
plt.xlabel("Класс каюты", fontsize=11)
plt.ylabel("Доля пассажиров, %", fontsize=11)
plt.ylim(0, 105)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()