import tkinter as tk


def create_window(name: str, width: int, height: int):
    window = tk.Tk()
    window.title(name)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)
    window.geometry(f"{width}x{height}+{center_x}+{center_y}")
    window.mainloop()
    return window


def login_window(width: int, height: int):
    window = create_window("Login", width, height)
    user_label = tk.Label(
        text="Username: ",
        fg="black",
        bg="white",
        width=15,
        height=5
    )
    password_label = tk.Label(
        text="Password: ",
        width=15,
        height=5,
        fg="black",
        bg="white"
    )

    user_label.place(x=70, y=20)
    password_label.place(x=70, y=40)
