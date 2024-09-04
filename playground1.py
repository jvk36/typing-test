import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import random

# ChatGPT Prompt:
# Could you come up with a basic desktop app built using Python/tkinter that 
# displays a title, some explanation, a read-only single-line edit box titled 
# "Current Highest Score". The edit box should show the current time and have 
# space for about 30 characters of additional text. Below that should be a 
# read-only multi-line edit box that contain 200 or so random words with the 
# first word highlighted. Below that should be another multi-line edit box that 
# allows users to type in the words in the first edit box. The program should 
# start a 60-second timer as soon as the user starts typing. The highlight in 
# the first edit-box should update as the user continue typing. Words per minute 
# (WPM) and the Timer should be shown below the edit box and should update as the 
# user types. 

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
        self.score_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
        
        self.start_time = None
        self.timer_running = False
        self.total_words = len(self.words)
        
    def generate_random_words(self, num_words=200):
        word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
                     "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli",
                     "violet", "watermelon", "xigua", "yellowfruit", "zucchini"] * 10
        random.shuffle(word_list)
        return word_list[:num_words]
    
    def update_words_text(self):
        self.words_text.delete(1.0, tk.END)
        highlighted_word = self.words[self.highlighted_word_index]
        self.words_text.insert(tk.END, " ".join(self.words))
        self.words_text.tag_add("highlight", "1.0", f"1.{len(highlighted_word)}")
        self.words_text.tag_configure("highlight", background="yellow")
    
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
        self.wpm_label.config(text=f"WPM: {wpm}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
