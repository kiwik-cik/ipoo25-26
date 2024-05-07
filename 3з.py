import numpy as np

# Создаем двумерный массив 3x4 из случайных чисел с плавающей запятой
# из нормального распределения с параметрами среднее=0, отклонение=1.0
random_array = np.random.normal(loc=0, scale=1.0, size=(3, 4))
print("Двумерный массив:")
print(random_array)

# Преобразуем двумерный массив в одномерный массив
flat_array = random_array.flatten()
print("\nОдномерный массив:")
print(flat_array)