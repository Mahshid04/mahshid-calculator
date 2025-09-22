import customtkinter as ctk


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mahshid Calculator (:")
        self.geometry("450x550")
        self.configure(bg="#f0f0f0")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ctk.CTkEntry(
            self,
            font=("Arial", 50),
            fg_color="#87ceeb",
            corner_radius=30,
            height=70,
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10), sticky="nsew")


        main_frame = ctk.CTkFrame(self, fg_color="#c2d4ae")
        main_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")


        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
            main_frame.rowconfigure(i, weight=1)


        self.create_button("1", main_frame, 0, 0, lambda: self.add_number(1))
        self.create_button("2", main_frame, 0, 1, lambda: self.add_number(2))
        self.create_button("3", main_frame, 0, 2, lambda: self.add_number(3))
        self.create_button("+", main_frame, 0, 3, lambda: self.add_operation("+"))

        self.create_button("4", main_frame, 1, 0, lambda: self.add_number(4))
        self.create_button("5", main_frame, 1, 1, lambda: self.add_number(5))
        self.create_button("6", main_frame, 1, 2, lambda: self.add_number(6))
        self.create_button("-", main_frame, 1, 3, lambda: self.add_operation("-"))

        self.create_button("7", main_frame, 2, 0, lambda: self.add_number(7))
        self.create_button("8", main_frame, 2, 1, lambda: self.add_number(8))
        self.create_button("9", main_frame, 2, 2, lambda: self.add_number(9))
        self.create_button("/", main_frame, 2, 3, lambda: self.add_operation("/"))

        self.create_button("C", main_frame, 3, 0, self.clear)
        self.create_button("0", main_frame, 3, 1, lambda: self.add_number(0))
        self.create_button("=", main_frame, 3, 2, self.calculate)
        self.create_button("*", main_frame, 3, 3, lambda: self.add_operation("*"))

    def create_button(self, text, frame, row, column, command, fg_color="#eeefea"):
        button = ctk.CTkButton(
            frame,
            text=text,
            command=command,
            font=("Arial", 40),
            text_color="#003366",
            fg_color=fg_color,
            corner_radius=10
        )
        button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def add_number(self, number):
        current = self.entry.get()
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, current + str(number))

    def add_operation(self, operation):
        current = self.entry.get()
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, current + operation)

    def calculate(self):
        try:
            current = self.entry.get()
            result = eval(current)
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, "Error!")

    def clear(self):
        self.entry.delete(0, ctk.END)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
