import pandas as pd
import matplotlib.pyplot as plt
clean_data = pd.read_parquet("titanic.parquet")#переводим в цсв и сохраняем 
clean_data.to_csv("output.csv", index=False, encoding="utf-8")
passengers = pd.read_csv("output.csv")
stats = passengers.groupby(["Pclass", "Survived"]).size().unstack(fill_value=0)#расчет процентов 
percentages = stats.div(stats.sum(axis=1), axis=0) * 100
class_labels = ["Первый класс", "Второй класс", "Третий класс"]#офомление графика 
alive_share = percentages[1].values
dead_share = percentages[0].values
plt.figure(figsize=(9, 6))
plt.bar(class_labels, alive_share, width=0.55, color="#2E8B57", edgecolor="black", label="Выжившие")#оформление колонн
plt.bar(class_labels, dead_share, width=0.55, bottom=alive_share, color="#CD5C5C", edgecolor="black", label="Погибшие")
plt.title("Доля выживших и погибших пассажиров по классам (%)", fontsize=13, pad=12)#доп оформление
plt.xlabel("Класс каюты", fontsize=11)
plt.ylabel("Доля пассажиров, %", fontsize=11)
plt.ylim(0, 105)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()#отрисовка графика