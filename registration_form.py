import tkinter as tk
from tkinter import messagebox


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма регистрации")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Основной фрейм для формы
        main_frame = tk.Frame(root, padx=40, pady=40)
        main_frame.pack(expand=True, fill='both')
        
        # Заголовок
        title_label = tk.Label(main_frame, text="Регистрация", 
                               font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Поле: Имя пользователя
        username_label = tk.Label(main_frame, text="Имя пользователя:", 
                                  font=("Arial", 12))
        username_label.grid(row=1, column=0, sticky='w', pady=8)
        
        self.username_entry = tk.Entry(main_frame, width=30, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=8, padx=5)
        
        # Поле: Пароль
        password_label = tk.Label(main_frame, text="Пароль:", 
                                  font=("Arial", 12))
        password_label.grid(row=2, column=0, sticky='w', pady=8)
        
        self.password_entry = tk.Entry(main_frame, width=30, show="*", 
                                       font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=8, padx=5)
        
        # Поле: Подтверждение пароля
        confirm_label = tk.Label(main_frame, text="Подтверждение пароля:", 
                                font=("Arial", 12))
        confirm_label.grid(row=3, column=0, sticky='w', pady=8)
        
        self.confirm_entry = tk.Entry(main_frame, width=30, show="*", 
                                      font=("Arial", 12))
        self.confirm_entry.grid(row=3, column=1, pady=8, padx=5)
        
        # Метка для сообщений об ошибках
        self.error_label = tk.Label(main_frame, text="", 
                                    font=("Arial", 10), fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, pady=15)
        
        # Кнопка регистрации
        register_button = tk.Button(main_frame, text="Зарегистрироваться", 
                                    font=("Arial", 13, "bold"),
                                    bg="#4CAF50", fg="white",
                                    padx=30, pady=10,
                                    command=self.register)
        register_button.grid(row=5, column=0, columnspan=2, pady=15)
        
        # Привязка Enter к кнопке регистрации
        self.root.bind('<Return>', lambda event: self.register())
    
    def register(self):
        """Обработка регистрации с проверками"""
        # Очистка предыдущих сообщений об ошибках
        self.error_label.config(text="")
        
        # Получение значений из полей
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()
        
        # Проверка: заполнены ли все поля
        if not username:
            self.error_label.config(text="Ошибка: Введите имя пользователя!")
            self.username_entry.focus()
            return
        
        if not password:
            self.error_label.config(text="Ошибка: Введите пароль!")
            self.password_entry.focus()
            return
        
        if not confirm_password:
            self.error_label.config(text="Ошибка: Подтвердите пароль!")
            self.confirm_entry.focus()
            return
        
        # Проверка: совпадают ли пароли
        if password != confirm_password:
            self.error_label.config(text="Ошибка: Пароли не совпадают!")
            self.password_entry.delete(0, tk.END)
            self.confirm_entry.delete(0, tk.END)
            self.password_entry.focus()
            return
        
        # Успешная регистрация
        messagebox.showinfo("Успех", 
                           f"Регистрация прошла успешно!\n"
                           f"Добро пожаловать, {username}!")
        
        # Очистка полей после успешной регистрации
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_entry.delete(0, tk.END)
        self.username_entry.focus()


def main():
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()


if __name__ == "__main__":
    main()
