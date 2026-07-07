import customtkinter as ctk
import json
import os

# ==========================
# НАСТРОЙКИ
# ==========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

TASKS_FILE = "tasks.json"

# ==========================
# ФУНКЦИИ
# ==========================


def update_counter():
    count = len(task_frame.winfo_children())
    counter_label.configure(text=f"📋 Всего задач: {count}")


def save_tasks():
    tasks = []

    for checkbox in task_frame.winfo_children():

        if isinstance(checkbox, ctk.CTkCheckBox):

            tasks.append(
                {
                    "text": checkbox.cget("text"),
                    "checked": bool(checkbox.get())
                }
            )

    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def create_task(text, checked=False):

    checkbox = ctk.CTkCheckBox(
        master=task_frame,
        text=text,
        font=("Arial", 16),
        command=save_tasks
    )

    checkbox.pack(
        anchor="w",
        padx=10,
        pady=5
    )

    if checked:
        checkbox.select()

    update_counter()

def update_counter():
    count = 0

    for widget in task_frame.winfo_children():
        if isinstance(widget, ctk.CTkCheckBox):
            count += 1

    counter_label.configure(text=f"📋 Всего задач: {count}")


def add_task():

    task = task_entry.get().strip()

    if task == "":
        return

    create_task(task)

    task_entry.delete(0, "end")

    save_tasks()
    update_counter()


def load_tasks():

    if not os.path.exists(TASKS_FILE):
        return

    try:

        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)

    except json.JSONDecodeError:

        tasks = []

    for task in tasks:

        create_task(
            task["text"],
            task["checked"]
        )


def clear_tasks():

    for widget in task_frame.winfo_children():
        widget.destroy()

    save_tasks()
    update_counter()


# ==========================
# ОКНО
# ==========================

app = ctk.CTk()

app.title("To-Do List")

app.geometry("500x650")

app.resizable(False, False)

# ==========================
# ЗАГОЛОВОК
# ==========================

title = ctk.CTkLabel(
    app,
    text="📝 TO-DO LIST",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)

counter_label = ctk.CTkLabel(
    app,
    text="📋 Всего задач: 0",
    font=("Arial", 16)
)

counter_label.pack(pady=(0, 15))

# ==========================
# ПОЛЕ ВВОДА
# ==========================

task_entry = ctk.CTkEntry(
    app,
    placeholder_text="Введите новую задачу...",
    width=360,
    height=40,
    font=("Arial", 16)
)

task_entry.pack(pady=10)

# ==========================
# КНОПКИ
# ==========================

buttons_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

buttons_frame.pack(pady=10)

add_button = ctk.CTkButton(
    buttons_frame,
    text="Добавить задачу",
    width=170,
    height=40,
    command=add_task
)

add_button.pack(
    side="left",
    padx=5
)

clear_button = ctk.CTkButton(
    buttons_frame,
    text="Очистить всё",
    width=170,
    height=40,
    fg_color="#d9534f",
    hover_color="#c9302c",
    command=clear_tasks
)

clear_button.pack(
    side="left",
    padx=5
)

# Добавление задачи по Enter
task_entry.bind("<Return>", lambda event: add_task())

# ==========================
# СПИСОК ЗАДАЧ
# ==========================

task_frame = ctk.CTkScrollableFrame(
    app,
    width=440,
    height=360
)

task_frame.pack(
    pady=20,
    padx=20,
    fill="both",
    expand=True
)

# ==========================
# ЗАГРУЗКА ДАННЫХ
# ==========================

load_tasks()

update_counter()

# ==========================
# ЗАПУСК
# ==========================

app.mainloop()