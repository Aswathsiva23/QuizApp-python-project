import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # PIL is needed to handle images in Tkinter

# Sample Questions and Answers
questions = [
    ("What is the capital of France?", "Paris", ["Paris", "London", "Berlin", "Madrid"]),
    ("What is the largest planet?", "Jupiter", ["Earth", "Venus", "Jupiter", "Mars"]),
    ("What language is used for Android development?", "Java", ["Python", "Swift", "Java", "Kotlin"]),
    ("What is the speed of light?", "299792458 m/s", ["300000000 m/s", "299792458 m/s", "150000000 m/s", "299792500 m/s"]),
]

# Initialize quiz state
current_question = 0
score = 0

# Function to load a question
def load_question():
    global current_question
    question_text, correct_answer, options = questions[current_question]
    question_label.config(text=question_text)
    for i, option in enumerate(options):
        radio_buttons[i].config(text=option)
    answer_var.set(None)  # Reset selected answer

# Function to check the answer
def check_answer():
    global current_question, score
    selected_option = answer_var.get()
    correct_answer = questions[current_question][1]
    
    if selected_option == correct_answer:
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong! The correct answer was: {correct_answer}")
    
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        show_score()

# Function to display the final score
def show_score():
    messagebox.showinfo("Quiz Finished", f"Your score is: {score}/{len(questions)}")
    app.quit()

# Setting up the GUI window
app = tk.Tk()
app.title("Quiz App")
app.geometry("600x400")  # Set the size of the window

# Load background image
background_image = Image.open("C:\Users\ADMIN\OneDrive\Desktop\Full stack\Prakash img.jpg ")
background_photo = ImageTk.PhotoImage(background_image.resize((600, 400)))

# Create a Canvas for the background
canvas = tk.Canvas(app, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Place the question and options on top of the background image
question_label = tk.Label(app, text="", font=("Arial", 14), wraplength=400, justify="center", bg="white")
canvas.create_window(300, 50, window=question_label)

answer_var = tk.StringVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(app, text="", variable=answer_var, value="", font=("Arial", 12), bg="white")
    canvas.create_window(300, 120 + i*40, window=rb)
    radio_buttons.append(rb)

# Submit Button
submit_button = tk.Button(app, text="Submit Answer", command=check_answer, font=("Arial", 12), bg="lightblue")
canvas.create_window(300, 300, window=submit_button)

# Load the first question
load_question()

# Run the app
app.mainloop()
