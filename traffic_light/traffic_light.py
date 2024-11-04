import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Светофор")
root.geometry("200x250")  # Задаем размеры окна

# Функция для обновления цвета кнопок и метки
def update_light(color):
    # Устанавливаем серый цвет для всех кнопок
    red_button.config(bg="gray")
    yellow_button.config(bg="gray")
    green_button.config(bg="gray")

    # Меняем цвет нажатой кнопки и текст метки
    if color == "red":
        red_button.config(bg="#ff0000")
        label.config(text="Стой – красный свет!")
    elif color == "yellow":
        yellow_button.config(bg="#ffff00")
        label.config(text="Жди – жёлтый свет!")
    elif color == "green":
        green_button.config(bg="#00ff00")
        label.config(text="Иди – зелёный свет!")


# Создаем метку для сообщения
label = tk.Label(root, text="", font=("Helvetica", 14))
label.pack(pady=10)

# Создаем кнопки для светофора
red_button = tk.Button(root, text="Красный", width=10, height=2, bg="gray", command=lambda: update_light("red"))
red_button.pack(pady=5)

yellow_button = tk.Button(root, text="Жёлтый", width=10, height=2, bg="gray", command=lambda: update_light("yellow"))
yellow_button.pack(pady=5)

green_button = tk.Button(root, text="Зелёный", width=10, height=2, bg="gray", command=lambda: update_light("green"))
green_button.pack(pady=5)

# Запускаем основной цикл
root.mainloop()
