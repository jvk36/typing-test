# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## APPLICATION - INTRO

This is a desktop application built using tkinter GUI library and the pillow library for image processing:

https://docs.python.org/3/library/tkinter.html
https://pypi.org/project/Pillow/

The application is self-contained in the main.py file. The rest of the python files introduces/tests the libraries used.

## main.py APPLICATION - FUNCTION DESCRIPTION:

The functionality is mostly embedded within the class TypingTestApp. Method details follow:

__init__: the constructor initializes the tkinter UI. 
generate_random_words: constructs the words list used for the typing test source text.
update_words_text, update_highlight: encapsulates the logic for highlighting the word the test taker needs to type next.
start_timer, update_timer: encapsulates the timer logic.
update_wpm, calculate_wpm: encapsulates the logic that keeps track of the words-per-minute.
reset_test, finish_test: encapsulates the logic that allows finishing and resetting the test.

## playground1.py through playground7.py - variations of the program tried in different steps:

NOTE: these programs were largely generated by ChatGPT 3.5. The prompts used for the first two are below. The rest did not improve the program much and so was abandoned. playground2.py was adapted to build the final main.py application.

1. playground1.py:  ChatGPT Prompt - Could you come up with a basic desktop app built using Python/tkinter that displays a title, some explanation, a read-only single-line edit box titled "Current Highest Score". The edit box should show the current time and have space for about 30 characters of additional text. Below that should be a read-only multi-line edit box that contain 200 or so random words with the first word highlighted. Below that should be another multi-line edit box that allows users to type in the words in the first edit box. The program should start a 60-second timer as soon as the user starts typing. The highlight in the first edit-box should update as the user continue typing. Words per minute (WPM) and the Timer should be shown below the edit box and should update as the user types.

2. playground2.py: ChatGPT Prompt - Could you make the following changes? – a) The “Current Highest Score” box should show the current time & highest WPM so far – it is empty now, b) Add a Reset button that clears the typed input and starts the timer only after the user starts typing. Also repopulate the “Text to Type” so that it is not the same when retaking the test, c) The words are homogenous (name of fruits) – could you make it more random?, and d) The highlighting is not working. It highlights the first word and parts of that word as the user types. It should highlight the word the user is typing.

## tkinter_intro - tkinter library intro:

The self-contained program shows a basic UI with a Background Image, Label, an Edit Box and a Button. Typing something into the Edit Box and Clicking the Button will result in the Label getting updated with what was typed in. 

## pillow_intro - pillow library intro:

The self-contained test program shows how to use the library to convert a png image to different formats - jpg, webp, and thumbnail.

