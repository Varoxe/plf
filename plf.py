import tkinter as tk
from tkinter import messagebox

class LanguageFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLF - Programming Language Finder")
        
        self.question_label = tk.Label(root, text="Hello, I'm Varoxe and I want to help you find the right programming language for you.\nI will ask you some questions and then I will tell you which programming language you should learn.", wraplength=400)
        self.question_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)
        
        self.response_entry = tk.Entry(root)
        self.response_entry.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_response)
        self.submit_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="", wraplength=400)
        self.result_label.pack(pady=10)
        
        self.lang_dict = self.language()
        self.current_question = 0
        self.questions = [
            "What do you want to learn?\n1) Creating websites\n2) Creating games\n3) Creating mobile apps\n4) Creating desktop apps\n5) Creating AI\n6) Creating automation programs"
        ]
        
    def start_test(self):
        self.current_question = 0
        self.show_question()
        
    def show_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.question_label.config(text="Test completed.")
            self.start_button.pack(pady=5)
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
                "You should learn HTML, CSS and JavaScript.\n"
                "If you want to learn more about web development, you should visit w3schools.com\n"
                "w3schools HTML - https://www.w3schools.com/html/default.asp\n"
                "w3schools CSS - https://www.w3schools.com/css/default.asp\n"
                "w3schools JavaScript - https://www.w3schools.com/js/default.asp\n"
            ),
            'game': (
                "You should learn C# and Unity.\n"
                "If you want to learn more about game development, you should visit unity.com\n"
                "Unity - https://unity.com/\n"
            ),
            'mobile': (
                "You should learn Java or Kotlin.\n"
                "If you want to learn more about mobile development, you should visit developer.android.com\n"
                "Android Developer - https://developer.android.com/\n"
            ),
            'software': (
                "You should learn Python.\n"
                "If you want to learn more about software development, you should visit python.org\n"
                "Python - https://www.python.org/\n"
            ),
            'ai': (
                "You should learn Python and TensorFlow.\n"
                "If you want to learn more about AI, you should visit tensorflow.org\n"
                "TensorFlow - https://www.tensorflow.org/\n"
            ),
            'automation': (
                "You should learn Python.\n"
                "If you want to learn more about automation, you should visit python.org\n"
                "Python - https://www.python.org/\n"
            )
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageFinderApp(root)
    root.mainloop()