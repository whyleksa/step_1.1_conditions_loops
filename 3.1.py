#Задание 1: “Угадай число”
import random

number = random.randint(1,10)
attempts = 5

print("Угадай число от 1 до 10! У тебя 5 попыток")

while attempts > 0:
    guess = int(input("Введи число: "))
    attempts -= 1

    if guess == number:
        print("!!!Ура, ты угадал!!!")
        break
    elif guess < number:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")

    if attempts > 0:
        print(f"Осталось попыток: {attempts}\n")
    else:
        print(f"Попытки закончились! Я загадал {number}")