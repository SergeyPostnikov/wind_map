import noise
import math

def generate_wind_field(size):
    # определяем параметры генерации шума
    scale = 50.0
    octaves = 3
    persistence = 0.5
    lacunarity = 2.0
    
    # создаем пустой массив для значений силы и направления ветра
    wind_field = []
    
    # генерируем значения шума для каждой точки поля
    for i in range(size):
        row = []
        for j in range(size):
            # получаем значение шума в диапазоне от -1 до 1
            value = noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
            # вычисляем угол направления ветра в градусах
            angle = math.degrees(math.atan2(value, 1))
            # вычисляем силу ветра
            magnitude = math.sqrt(value**2 + 1)
            # добавляем значение силы и направления ветра в массив
            row.append((magnitude, angle))
        wind_field.append(row)
    
    return wind_field
