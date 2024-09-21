import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LanguageFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLF - Programming Language Finder")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2e")

        # Stil konfigurieren
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=6, relief="flat", foreground="white", background="#3b3b4d")
        style.map("TButton", background=[('active', '#575766')])

        style.configure("TLabel", font=("Segoe UI", 12), foreground="white", background="#1e1e2e")

        # Rahmen für das Layout
        frame = tk.Frame(root, bg="#1e1e2e")
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Textfeld für die Fragen
        self.question_label = tk.Label(
            frame,
            text=("Hello, I'm Varoxe, and I want to help you find the right programming language for you.\n"
                  "I will ask you some questions and then suggest which programming language you should learn."),
            wraplength=450,
            fg="white", bg="#1e1e2e", font=("Segoe UI", 12)
        )
        self.question_label.pack(pady=20)

        # Eingabefeld für die Antworten
        self.response_entry = tk.Entry(
            frame, bg="#3b3b4d", fg="white", font=("Segoe UI", 12),
            insertbackground="white", relief="flat", width=30
        )
        self.response_entry.pack(pady=10)

        # Start-Button
        self.start_button = tk.Button(
            frame, text="Start Test", command=self.start_test,
            bg="#3b3b4d", fg="white", font=("Segoe UI", 12), relief="flat", activebackground="#575766"
        )
        self.start_button.pack(pady=10)

        # Button zum Absenden der Antwort
        self.submit_button = tk.Button(
            frame, text="Submit", command=self.submit_response,
            bg="#3b3b4d", fg="white", font=("Segoe UI", 12), relief="flat", activebackground="#575766"
        )
        self.submit_button.pack(pady=10)

        # Ergebnis-Label
        self.result_label = tk.Label(frame, text="", wraplength=450, fg="white", bg="#1e1e2e", font=("Segoe UI", 12))
        self.result_label.pack(pady=20)

        # Initialisieren der Sprachen-Liste und der Fragen
        self.lang_dict = self.language()
        self.current_question = 0
        self.questions = [
            "What do you want to learn?\n1) Creating websites\n2) Creating games\n"
            "3) Creating mobile apps\n4) Creating desktop apps\n5) Creating AI\n6) Creating automation programs"
        ]

    def start_test(self):
        self.current_question = 0
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.question_label.config(text="Test completed.")
            self.response_entry.pack_forget()
            self.submit_button.pack_forget()

    def submit_response(self):
        answer = self.response_entry.get().strip()
        if self.current_question == 0:
            try:
                answer = int(answer)
                if 1 <= answer <= 6:
                    option = {
                        1: 'web',
                        2: 'game',
                        3: 'mobile',
                        4: 'software',
                        5: 'ai',
                        6: 'automation'
                    }
                    choice = option.get(answer)
                    if choice in self.lang_dict:
                        self.result_label.config(text=self.lang_dict[choice])
                    else:
                        self.result_label.config(text="Error: Invalid choice.")
                else:
                    messagebox.showerror("Invalid Input", "Please enter a number between 1 and 6.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
        self.current_question += 1
        self.show_question()

    def language(self):
        return {
            'web': (
                "You should learn HTML, CSS, and JavaScript.\n"
                "Learn more: w3schools HTML - https://www.w3schools.com/html/default.asp\n"
                "w3schools CSS - https://www.w3schools.com/css/default.asp\n"
                "w3schools JavaScript - https://www.w3schools.com/js/default.asp"
            ),
            'game': (
                "You should learn C# and Unity.\n"
                "Learn more: Unity - https://unity.com/"
            ),
            'mobile': (
                "You should learn Java or Kotlin.\n"
                "Learn more: Android Developer - https://developer.android.com/"
            ),
            'software': (
                "You should learn Python.\n"
                "Learn more: Python - https://www.python.org/"
            ),
            'ai': (
                "You should learn Python and TensorFlow.\n"
                "Learn more: TensorFlow - https://www.tensorflow.org/"
            ),
            'automation': (
                "You should learn Python and Selenium.\n"
                "Learn more: Python - https://www.python.org/"
            )
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageFinderApp(root)
    root.mainloop()