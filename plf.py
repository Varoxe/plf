import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LanguageFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLF - Programming Language Finder")
        self.root.geometry("600x600")
        self.root.configure(bg="#1e1e2e")

        # Stil konfigurieren
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=6, relief="flat", foreground="white", background="#3b3b4d")
        style.map("TButton", background=[('active', '#575766')])
        style.configure("TLabel", font=("Segoe UI", 12), foreground="white", background="#1e1e2e")

        # Frame für den Titel
        title_frame = tk.Frame(root, bg="#1e1e2e")
        title_frame.pack(pady=10)
        
        # Rahmen für das Layout
        frame = tk.Frame(root, bg="#1e1e2e")
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Einführungstext
        intro_text = ("Hello, I'm Varoxe, and I want to help you find the right programming language for you.\n"
                      "I will ask you some questions and then suggest which programming language you should learn.")
        self.intro_label = tk.Label(frame, text=intro_text, wraplength=450, fg="white", bg="#1e1e2e", font=("Segoe UI", 12))
        self.intro_label.pack(pady=20)

        # Textfeld für die Fragen
        self.question_label = tk.Label(frame, text="Frage:", font=("Segoe UI", 12), fg="white", bg="#1e1e2e")
        self.question_label.pack(pady=10)

        # Variable für die Antwort
        self.answer_var = tk.StringVar()

        # Radiobuttons für die Antworten
        self.radio_buttons = []
        for i in range(5):
            rb = tk.Radiobutton(frame, text="", variable=self.answer_var, value=str(i), font=("Segoe UI", 12), fg="white", bg="#1e1e2e", selectcolor="#3b3b4d")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        # Stil für den Button konfigurieren
        style.configure("Blue.TButton", font=("Segoe UI", 12), padding=6, relief="flat", foreground="black", background="blue")
        style.map("Blue.TButton", background=[('active', 'blue')])

        # Button zum Absenden der Antwort
        self.submit_button = ttk.Button(frame, text="Submit", style="Blue.TButton", command=self.submit_response)
        self.submit_button.pack(pady=10)

        # Ergebnis-Label
        self.result_label = tk.Label(frame, text="", wraplength=450, fg="white", bg="#1e1e2e", font=("Segoe UI", 12))
        self.result_label.pack(pady=20)

        # Initialisieren der Sprachen-Liste und der Fragen
        self.lang_dict = self.language()
        self.current_question = 0
        self.responses = []
        self.questions = [
            ("What is your main goal in programming?", [
                "a) Web development",
                "b) Game development",
                "c) Data analysis",
                "d) Artificial intelligence",
                "e) Task automation"
            ]),
            ("Do you have any experience with a programming language? If so, which one?", [
                "a) Yes, I know Python.",
                "b) Yes, I know Java.",
                "c) Yes, I know JavaScript.",
                "d) No, I have no experience.",
                "e) I know a little of several languages."
            ]),
            ("How much time do you want to invest in learning?", [
                "a) At least one hour daily",
                "b) Several times a week",
                "c) Only on weekends",
                "d) Occasionally, when I have time",
                "e) I want to learn spontaneously whenever I feel like it"
            ]),
            ("Do you prefer a language with simple syntax, or are you willing to learn a more complex one?", [
                "a) I prefer a simple syntax.",
                "b) I am willing to learn a complex language.",
                "c) Syntax doesn’t matter as long as I can learn.",
                "d) I want a mix of both.",
                "e) I’m not sure."
            ]),
            ("What is important to you in a programming language?", [
                "a) Strong community and support",
                "b) Extensive libraries and frameworks",
                "c) High performance",
                "d) Easy learning curve",
                "e) Flexibility in application"
            ]),
            ("What type of projects are you interested in?", [
                "a) Mobile apps",
                "b) Desktop applications",
                "c) Web applications",
                "d) Data science and analytics",
                "e) Internet of Things (IoT)"
            ]),
            ("How important is platform independence to you?", [
                "a) Very important; I want to work everywhere.",
                "b) Important, but not critical.",
                "c) I don’t care; I mostly work on one system.",
                "d) I prefer specific platforms.",
                "e) I haven’t thought about it yet."
            ]),
            ("Are you interested in developing software that interacts with hardware?", [
                "a) Yes, I find that exciting!",
                "b) Maybe, if it’s easy to learn.",
                "c) I’m not sure what that means.",
                "d) No, I’m not interested in that.",
                "e) I prefer software development without hardware."
            ]),
            ("Do you have specific interests, such as machine learning or blockchain development?", [
                "a) Yes, I’m interested in machine learning.",
                "b) Yes, I’m interested in blockchain development.",
                "c) I’m interested in data analysis.",
                "d) I don’t have a specific interest.",
                "e) I want to try everything."
            ]),
            ("How important is job marketability in the language you want to learn?", [
                "a) Very important; I’m looking for career opportunities.",
                "b) Important, but not the only criterion.",
                "c) I think that will take care of itself.",
                "d) I’m learning just for the fun of programming.",
                "e) I don’t care; I’m doing this as a hobby."
            ])
        ]

        self.start_test()

    def start_test(self):
        self.current_question = 0
        self.responses = []
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question, options = self.questions[self.current_question]
            self.question_label.config(text=question)
            for i, option in enumerate(options):
                self.radio_buttons[i].config(text=option, value=option)
            self.answer_var.set(None)
        else:
            recommended_language, language_info = self.evaluate_responses()
            self.result_label.config(text=f"Thank you for completing the survey! \nWe recommend you to learn {recommended_language}.\n\n{language_info[0]}\n\nFor more information, visit: {language_info[1]}")

    def submit_response(self):
        response = self.answer_var.get()
        if response:
            self.responses.append(response)
            self.current_question += 1
            self.show_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer before proceeding.")

    def evaluate_responses(self):
        scores = {
            "Python": 0,
            "JavaScript": 0,
            "Java": 0,
            "C++": 0,
            "Ruby": 0
        }

        for response in self.responses:
            if response == "a) Web development":
                scores["JavaScript"] += 1
                scores["Python"] += 1
                scores["Ruby"] += 1
            elif response == "b) Game development":
                scores["C++"] += 1
                scores["Java"] += 1
                scores["Python"] += 1
            elif response == "c) Data analysis":
                scores["Python"] += 1
            elif response == "d) Artificial intelligence":
                scores["Python"] += 1
                scores["C++"] += 1
            elif response == "e) Task automation":
                scores["Python"] += 1
                scores["Ruby"] += 1
            elif response == "a) Yes, I know Python.":
                scores["Python"] += 1
            elif response == "b) Yes, I know Java.":
                scores["Java"] += 1
            elif response == "c) Yes, I know JavaScript.":
                scores["JavaScript"] += 1
            elif response == "d) No, I have no experience.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "e) I know a little of several languages.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "a) At least one hour daily":
                scores["Python"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
            elif response == "b) Several times a week":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "c) Only on weekends":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "d) Occasionally, when I have time":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "e) I want to learn spontaneously whenever I feel like it":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "a) I prefer a simple syntax.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Ruby"] += 1
            elif response == "b) I am willing to learn a complex language.":
                scores["C++"] += 1
                scores["Java"] += 1
            elif response == "c) Syntax doesn’t matter as long as I can learn.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "d) I want a mix of both.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "e) I’m not sure.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "a) Strong community and support":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "b) Extensive libraries and frameworks":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "c) High performance":
                scores["C++"] += 1
                scores["Java"] += 1
            elif response == "d) Easy learning curve":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Ruby"] += 1
            elif response == "e) Flexibility in application":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "a) Mobile apps":
                scores["Java"] += 1
                scores["JavaScript"] += 1
                scores["Python"] += 1
            elif response == "b) Desktop applications":
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Python"] += 1
            elif response == "c) Web applications":
                scores["JavaScript"] += 1
                scores["Python"] += 1
                scores["Ruby"] += 1
            elif response == "d) Data science and analytics":
                scores["Python"] += 1
            elif response == "e) Internet of Things (IoT)":
                scores["Python"] += 1
                scores["C++"] += 1
            elif response == "a) Very important; I want to work everywhere.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "b) Important, but not critical.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "c) I don’t care; I mostly work on one system.":
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "d) I prefer specific platforms.":
                scores["Java"] += 1
                scores["C++"] += 1
            elif response == "e) I haven’t thought about it yet.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "a) Yes, I find that exciting!":
                scores["C++"] += 1
                scores["Python"] += 1
            elif response == "b) Maybe, if it’s easy to learn.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "c) I’m not sure what that means.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "d) No, I’m not interested in that.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "e) I prefer software development without hardware.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "a) Yes, I’m interested in machine learning.":
                scores["Python"] += 1
                scores["C++"] += 1
            elif response == "b) Yes, I’m interested in blockchain development.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "c) I’m interested in data analysis.":
                scores["Python"] += 1
            elif response == "d) I don’t have a specific interest.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "e) I want to try everything.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
                scores["C++"] += 1
                scores["Ruby"] += 1
            elif response == "a) Very important; I’m looking for career opportunities.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "b) Important, but not the only criterion.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
                scores["Java"] += 1
            elif response == "c) I think that will take care of itself.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "d) I’m learning just for the fun of programming.":
                scores["Python"] += 1
                scores["JavaScript"] += 1
            elif response == "e) I don’t care; I’m doing this as a hobby.":
                scores["Python"] += 1
                scores["JavaScript"] += 1

        # Die Programmiersprache mit der höchsten Punktzahl zurückgeben
        recommended_language = max(scores, key=scores.get)
        language_info = self.language_info(recommended_language)
        return recommended_language, language_info

    def language_info(self, language):
        info = {
            "Python": ("Python is a versatile language used for web development, data analysis, artificial intelligence, and more.", "https://www.python.org/"),
            "JavaScript": ("JavaScript is essential for web development, enabling interactive web pages and web applications.", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"),
            "Java": ("Java is widely used for building enterprise-scale applications, mobile apps, and large systems.", "https://www.java.com/"),
            "C++": ("C++ is a powerful language used for system/software development, game development, and performance-critical applications.", "https://isocpp.org/"),
            "Ruby": ("Ruby is known for its simplicity and productivity, often used in web development with the Ruby on Rails framework.", "https://www.ruby-lang.org/")
        }
        return info.get(language, ("Information not available", ""))
    
    def language(self):
        return {
            "Python": "Creating websites, Creating games, Creating mobile apps, Creating desktop apps, Creating AI, Creating automation programs",
            "JavaScript": "Creating websites, Creating games, Creating mobile apps",
            "Java": "Creating mobile apps, Creating desktop apps, Creating games",
            "C++": "Creating games, Creating desktop apps, Creating AI",
            "Ruby": "Creating websites, Creating automation programs"
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageFinderApp(root)
    root.mainloop()