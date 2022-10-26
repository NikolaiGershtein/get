import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Вызов файлов 
with open("settings2.txt", "r") as settings:
    settings_array=[float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data2.txt", dtype=int)

# Получение массива с показаниями
data_arrayvl=data_array * settings_array[0]
time=np.array([i*settings_array[1] for i in range(data_arrayvl.size)])

# Задания поля графика и масштабы
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.axis([time.min(), time.max(), data_arrayvl.min(), data_arrayvl.max()+0.2])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))


#  Подпись осей
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

# Название графика
ax.set_title("\n".join(wrap('Зарядка и разрядка конденсатора в RC-цепи' , 60)))


# Постороение сетки графика
ax.minorticks_on()
ax.grid(which='major', color = 'gray', linewidth=2)
ax.grid(which='minor', color = 'gray', linestyle= ':')
#Время работы
plt.text(5,3.25, 'Время зарядки = 4,25 с')
plt.text(5,3.1, 'Время разрядки = 6,75 с')

#Легенда графика
ax.plot(time, data_arrayvl, 'o', ls='-', ms=4,markevery=10,  label = 'U(t)', color= 'black')

#Сохранение графика в файл. 
ax.legend()
fig.savefig("graph.png")
fig.savefig("graph.svg")
plt.show()