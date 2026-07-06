import customtkinter as ctk

# Настройки внешнего вида
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Главное окно
app = ctk.CTk()
app.title("To-Do List")
app.geometry("500x600")
app.resizable(False, False)

# Заголовок
title = ctk.CTkLabel(
    app,
    text="📝 TO-DO LIST",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

# Поле ввода
task_entry = ctk.CTkEntry(
    app,
    placeholder_text="Введите новую задачу...",
    width=350,
    height=40,
    font=("Arial", 16)
)
task_entry.pack(pady=10)
def add_task():

    task = task_entry.get().strip()

    if task == "":
        return

    checkbox = ctk.CTkCheckBox(
        task_frame,
        text=task,
        font=("Arial", 15)
    )

    checkbox.pack(anchor="w", padx=10, pady=5)

    task_entry.delete(0, "end")

# Кнопка
add_button = ctk.CTkButton(
    app,
    text="Добавить задачу",
    width=200,
    height=40,
    command=add_task
)
add_button.pack(pady=10)

# Список задач
task_frame = ctk.CTkScrollableFrame(
    app,
    width=420,
    height=330
)
task_frame.pack(pady=20)

app.mainloop()