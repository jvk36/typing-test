import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import random

# ChatGPT Prompt:
# Could you make the following changes? – a) The “Current Highest Score” box 
# should show the current time & highest WPM so far – it is empty now, b) Add 
# a Reset button that clears the typed input and starts the timer only after 
# the user starts typing. Also repopulate the “Text to Type” so that it is not 
# the same when retaking the test, c) The words are homogenous (name of fruits) – 
# could you make it more random?, and d) The highlighting is not working. It 
# highlights the first word and parts of that word as the user types. It should 
# highlight the word the user is typing. 

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test Application")
        
        # Title Label
        self.title_label = tk.Label(root, text="Typing Test Application", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Explanation Label
        self.explanation_label = tk.Label(root, text="Type the words below as quickly as possible.")
        self.explanation_label.pack(pady=5)
        
        # Read-only Single-line Edit Box
        self.score_label = tk.Label(root, text="Current Highest Score:")
        self.score_label.pack(pady=5)
        
        self.score_entry = tk.Entry(root, state='readonly', width=50)
        self.score_entry.insert(0, self.get_current_time())
        self.score_entry.pack(pady=5)
        
        # Read-only Multi-line Edit Box with random words
        self.words_label = tk.Label(root, text="Text to Type:")
        self.words_label.pack(pady=5)
        
        self.words_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50, state='normal')
        self.words = self.generate_random_words()
        self.highlighted_word_index = 0
        self.update_words_text()
        self.words_text.pack(pady=5)
        
        # User Input Multi-line Edit Box
        self.user_input_label = tk.Label(root, text="Your Typing Input:")
        self.user_input_label.pack(pady=5)
        
        self.user_input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
        self.user_input_text.pack(pady=5)
        self.user_input_text.bind("<KeyPress>", self.start_timer)
        self.user_input_text.bind("<KeyRelease>", self.update_highlight)
        
        # Timer and WPM Display
        self.timer_label = tk.Label(root, text="Timer: 0s")
        self.timer_label.pack(pady=5)
        
        self.wpm_label = tk.Label(root, text="WPM: 0")
        self.wpm_label.pack(pady=5)
        
        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test)
        self.reset_button.pack(pady=10)
        
        self.start_time = None
        self.timer_running = False
        self.highest_wpm = 0
        self.total_words = len(self.words)
        
    def generate_random_words(self, num_words=200):
        # Using a more varied list of words
        word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "house", "ice", "juice",
                     "kite", "lemon", "monkey", "notebook", "orange", "pencil", "queen", "rose", "sun", "tiger",
                     "umbrella", "vase", "wolf", "xylophone", "yellow", "zebra"] * 10
        random.shuffle(word_list)
        return word_list[:num_words]
    
    def update_words_text(self):
        self.words_text.config(state='normal')
        self.words_text.delete(1.0, tk.END)
        highlighted_word = self.words[self.highlighted_word_index]
        self.words_text.insert(tk.END, " ".join(self.words))
        self.words_text.tag_add("highlight", "1.0", f"1.{len(highlighted_word) + len(' '.join(self.words[:self.highlighted_word_index]))}")
        self.words_text.tag_configure("highlight", background="yellow")
        self.words_text.config(state='disabled')
    
    def start_timer(self, event):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()
    
    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Timer: {elapsed_time}s")
            self.root.after(1000, self.update_timer)
            if elapsed_time >= 60:
                self.timer_running = False
                self.calculate_wpm()
                self.finish_test()
            else:
                self.update_wpm()

    def update_wpm(self):
        typed_text = self.user_input_text.get(1.0, tk.END).strip()
        words_typed = len(typed_text.split())
        elapsed_time = max((time.time() - self.start_time) / 60, 1)  # avoid division by zero
        wpm = int(words_typed / elapsed_time)
        self.wpm_label.config(text=f"WPM: {wpm}")
    
    def update_highlight(self, event):
        typed_text = self.user_input_text.get(1.0, tk.END).strip()
        typed_words = typed_text.split()
        if len(typed_words) > 0 and typed_words[-1] == self.words[self.highlighted_word_index]:
            self.highlighted_word_index += 1
            if self.highlighted_word_index < len(self.words):
                self.update_words_text()
    
    def calculate_wpm(self):
        typed_text = self.user_input_text.get(1.0, tk.END).strip()
        words_typed = len(typed_text.split())
        elapsed_time = max((time.time() - self.start_time) / 60, 1)  # avoid division by zero
        wpm = int(words_typed / elapsed_time)
        if wpm > self.highest_wpm:
            self.highest_wpm = wpm
            # self.wpm_label.config(text=f"WPM: {self.highest_wpm}")
            self.score_entry.config(state='normal')
            self.score_entry.delete(0, tk.END)
            self.score_entry.insert(0, f"{self.get_current_time()}, Highest Score: {self.highest_wpm} WPM")
            self.score_entry.config(state='readonly')
    
    def reset_test(self):
        self.user_input_text.config(state='normal')
        self.user_input_text.delete(1.0, tk.END)
        self.highlighted_word_index = 0
        self.words = self.generate_random_words()
        self.update_words_text()
        self.start_time = None
        self.timer_running = False
        self.timer_label.config(text="Timer: 0s")
        self.wpm_label.config(text="WPM: 0")

    def finish_test(self):
        # self.user_input_text.delete(1.0, tk.END)
        self.user_input_text.config(state='disabled')
        self.start_time = None
        self.timer_running = False
        self.timer_label.config(text="Timer: 0s")

    def get_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
