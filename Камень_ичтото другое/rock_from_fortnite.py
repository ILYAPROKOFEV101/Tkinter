import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Список для хранения статистики игры
history = []
player_choices = {"rock": 0, "scissors": 0, "paiper": 0}


# Функция для обработки выбора игрока
def player_choice(choice):
    # Обновляем статистику выборов игрока
    player_choices[choice] += 1

    # Компьютер выбирает на основе статистики игрока
    computer_choice = intelligent_choice()

    # Загружаем соответствующее изображение для выбора компьютера
    if computer_choice == "rock":
        computer_image = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\rock.png").resize((80, 80)))
    elif computer_choice == "scissors":
        computer_image = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\scissors.png").resize((80, 80)))
    else:  # "paiper"
        computer_image = ImageTk.PhotoImage(
            Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\paiper.png").resize((80, 80)))

    # Обновление метки с выбором компьютера
    computer_label.config(text=f"Компьютер выбрал:")
    computer_choice_label.config(image=computer_image)
    computer_choice_label.image = computer_image  # Сохраняем ссылку на изображение, чтобы оно не исчезло

    # Логика для определения победителя
    if choice == computer_choice:
        result = "Ничья!"
    elif (choice == "rock" and computer_choice == "scissors") or \
            (choice == "scissors" and computer_choice == "paiper") or \
            (choice == "paiper" and computer_choice == "rock"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"

    # Обновление метки с результатом
    result_label.config(text=result)

    # Добавление статистики в историю
    history.append(
        f"Шаг {len(history) + 1}: Игрок: {choice.capitalize()}, Компьютер: {computer_choice.capitalize()}, Результат: {result}")

    # Обновление статистики
    update_history()


# Функции для обработки нажатия на кнопки
def on_rock_button_click():
    player_choice("rock")


def on_scissors_button_click():
    player_choice("scissors")


def on_paper_button_click():
    player_choice("paiper")


# Функция для выбора компьютера на основе статистики игрока
def intelligent_choice():
    # Находим, что чаще всего выбирает игрок
    most_chosen = max(player_choices, key=player_choices.get)

    # На основе выбора игрока, компьютер должен выбрать контрмеру
    if most_chosen == "rock":
        return "paiper"  # Бумага побеждает камень
    elif most_chosen == "scissors":
        return "rock"  # Камень побеждает ножницы
    elif most_chosen == "paiper":
        return "scissors"  # Ножницы побеждают бумагу
    else:
        return random.choice(["rock", "scissors", "paiper"])  # Если статистики нет, то выбираем случайно


# Функция для обновления статистики в интерфейсе
def update_history():
    # Очищаем текущую статистику
    history_text.delete(1.0, tk.END)

    # Выводим историю в текстовое поле
    for step in history:
        history_text.insert(tk.END, step + "\n")


# Создание основного окна
root = tk.Tk()
root.title("Камень, Ножницы, Бумага")

# Загружаем изображения для кнопок
rock_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\rock.png").resize((80, 80)))
scissors_image = ImageTk.PhotoImage(
    Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\scissors.png").resize((80, 80)))
paper_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Ilya\PycharmProjects\Uidev\res\paiper.png").resize((80, 80)))

# Кнопки для выбора игрока
rock_button = tk.Button(root, image=rock_image, command=on_rock_button_click)
rock_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, image=scissors_image, command=on_scissors_button_click)
scissors_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, image=paper_image, command=on_paper_button_click)
paper_button.pack(side=tk.LEFT, padx=10)

# Метка для отображения выбора компьютера
computer_label = tk.Label(root, text="Компьютер выбрал:", font=("Helvetica", 14))
computer_label.pack(pady=10)

# Метка для отображения изображения выбора компьютера
computer_choice_label = tk.Label(root)
computer_choice_label.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="Результат: ", font=("Helvetica", 14))
result_label.pack(pady=10)

# Поле для отображения статистики
history_label = tk.Label(root, text="Статистика игры:", font=("Helvetica", 14))
history_label.pack(pady=10)

history_text = tk.Text(root, width=50, height=10)
history_text.pack(pady=10)

# Запуск главного цикла
root.mainloop()
