import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import random

# ChatGPT Prompt:
# None of the problems got fixed. Can you attempt a rewrite and try to 
# fix everything?

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test Application")
        
        # Initialize variables
        self.words = []
        self.highlighted_word_index = 0
        self.start_time = None
        self.timer_running = False
        self.highest_wpm = 0
        self.elapsed_time = 0
        self.is_test_active = False

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
        self.update_score_display()
        self.score_entry.pack(pady=5)

        # Read-only Multi-line Edit Box with random words
        self.words_label = tk.Label(root, text="Text to Type:")
        self.words_label.pack(pady=5)

        self.words_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50, state='normal')
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
        
        # Initialize a new test
        self.reset_test()

    def generate_random_words(self, num_words=200):
        """Generate a list of random words."""
        word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "house", "ice", "juice",
                     "kite", "lemon", "monkey", "notebook", "orange", "pencil", "queen", "rose", "sun", "tiger",
                     "umbrella", "vase", "wolf", "xylophone", "yellow", "zebra"] * 10
        random.shuffle(word_list)
        return word_list[:num_words]

    def update_words_text(self):
        """Update the text in the read-only box with random words and highlight the current word."""
        self.words_text.config(state='normal')
        self.words_text.delete(1.0, tk.END)
        words_text = " ".join(self.words)
        self.words_text.insert(tk.END, words_text)
        
        # Highlight the current word
        start_index = self.get_word_start_index(self.highlighted_word_index)
        end_index = start_index + len(self.words[self.highlighted_word_index]) + 1
        self.words_text.tag_add("highlight", f"1.{start_index}", f"1.{end_index}")
        self.words_text.tag_configure("highlight", background="yellow")
        self.words_text.config(state='disabled')

    def get_word_start_index(self, index):
        """Calculate the start index of the word to be highlighted."""
        words_text = " ".join(self.words)
        return len(" ".join(self.words[:index])) + index + index  # Index + spaces

    def start_timer(self, event):
        """Start the timer when the user starts typing."""
        if not self.timer_running and self.is_test_active:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        """Update the timer display and stop after 60 seconds."""
        if self.timer_running:
            self.elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Timer: {self.elapsed_time}s")
            if self.elapsed_time >= 60:
                self.timer_running = False
                self.calculate_wpm()
                self.user_input_text.config(state='disabled')
            else:
                self.root.after(1000, self.update_timer)

    def update_highlight(self, event):
        """Update the highlight and WPM as the user types."""
        if self.is_test_active:
            typed_text = self.user_input_text.get(1.0, tk.END).strip()
            typed_words = typed_text.split()
            if typed_words and typed_words[-1] == self.words[self.highlighted_word_index]:
                self.highlighted_word_index += 1
                if self.highlighted_word_index < len(self.words):
                    self.update_words_text()
                self.calculate_wpm()  # Update WPM as user types

    def calculate_wpm(self):
        """Calculate and display the words per minute."""
        if self.start_time:
            typed_text = self.user_input_text.get(1.0, tk.END).strip()
            words_typed = len(typed_text.split())
            elapsed_time = max(self.elapsed_time / 60, 1)  # Avoid division by zero
            wpm = int(words_typed / elapsed_time)
            if wpm > self.highest_wpm:
                self.highest_wpm = wpm
            self.wpm_label.config(text=f"WPM: {self.highest_wpm}")
            self.update_score_display()

    def update_score_display(self):
        """Update the score display with the current highest WPM."""
        self.score_entry.config(state='normal')
        self.score_entry.delete(0, tk.END)
        self.score_entry.insert(0, f"{self.get_current_time()}, Words Per Minute – {self.highest_wpm}")
        self.score_entry.config(state='readonly')

    def reset_test(self):
        """Reset the test and start a new one."""
        self.user_input_text.delete(1.0, tk.END)
        self.words = self.generate_random_words()
        self.highlighted_word_index = 0
        self.update_words_text()
        self.start_time = None
        self.timer_running = False
        self.elapsed_time = 0
        self.timer_label.config(text="Timer: 0s")
        self.wpm_label.config(text="WPM: 0")
        self.user_input_text.config(state='normal')
        self.is_test_active = True

    def get_current_time(self):
        """Get the current time as a string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
