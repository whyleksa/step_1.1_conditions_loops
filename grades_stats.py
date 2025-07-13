#Задание 2: “Статистика оценок”

grades = [3, 4, 5, 2, 5, 3, 4]

# Подсчет средней оценки
average = sum(grades) / len(grades)
print(f'Средняя оценка: {average:.2f}')

# Подсчет количества оценок
fives = grades.count(5)
threes = grades.count(3)
twos = grades.count(2)

print(f'Пятёрок: {fives}')
print(f'Троек: {threes}')
print(f'Двоек: {twos}')

# Проверка наличия двоек
if 2 in grades:
    print('Есть хотя бы одна двойка!')
else:
    print('Двоек нет')