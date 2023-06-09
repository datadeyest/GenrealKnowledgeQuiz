import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define the quiz questions and answers
quiz_data = [
    ("What country has the highest life expectancy?", "Hong Kong"),
    ("Where would you be if you were standing on the Spanish Steps?", "Rome"),
    ("Which language has the more native speakers: English or Spanish?", "Spanish"),
    ("What is the most common surname in the United States?", "Smith"),
    ("What disease commonly spread on pirate ships?", "Scurvy"),
    ("Who was the Ancient Greek God of the Sun?", "Apollo"),
    ("What was the name of the crime boss who was head of the feared Chicago Outfit?", "Al Capone"),
    ("What year was the United Nations established?", "1945"),
    ("Who has won the most total Academy Awards?", "Walt Disney"),
    ("What artist has the most streams on Spotify?", "Drake"),
    ("How many minutes are in a full week?", "10,080"),
    ("What car manufacturer had the highest revenue in 2020?", "Volkswagen"),
    ("How many elements are in the periodic table?", "118"),
    ("What company was originally called 'Cadabra'?", "Amazon"),
    ("How many faces does a Dodecahedron have?", "12"),
    ("Queen guitarist Brian May is also an expert in what scientific field?", "Astrophysics"),
    ("Aureolin is a shade of what color?", "Yellow"),
    ("How many ghosts chase Pac-Man at the start of each game?", "4"),
    ("What Renaissance artist is buried in Rome's Pantheon?", "Raphael"),
    ("What shoe brand makes the 'Mexico 66'?", "Onitsuka Tiger"),
    ("What game studio makes the Red Dead Redemption series?", "Rockstar Games"),
    ("Who was the last Tsar of Russia?", "Nicholas II"),
    ("What character have both Robert Downey Jr. and Benedict Cumberbatch played?", "Sherlock Holmes"),
    ("What country drinks the most coffee per capita?", "Finland"),
    ("Which planet in the Milky Way is the hottest?", "Venus"),
    ("What is the 4th letter of the Greek alphabet?", "Delta"),
    ("What sports car company manufactures the 911?", "Porsche"),
    ("What city is known as 'The Eternal City'?", "Rome"),
    ("Roald Amundsen was the first man to reach the South Pole, but where was he from?", "Norway"),
    ("What is the highest-rated film on IMDb as of January 1st, 2022?", "The Shawshank Redemption"),
    ("Who discovered that the earth revolves around the sun?", "Nicolaus Copernicus"),
    ("What company was initially known as 'Blue Ribbon Sports'?", "Nike"),
    ("What art form is described as 'decorative handwriting or handwritten lettering'?", "Calligraphy"),
    ("Which planet has the most moons?", "Saturn"),
    ("What country has won the most World Cups?", "Brazil"),
    ("Complete the following lyrics - 'I should have changed that stupid lock.....'", "I should have made you leave your key"),
    ("Kratos is the main character of what video game series?", "God of War"),
    ("In what country would you find Mount Kilimanjaro?", "Tanzania"),
    ("What is a group of pandas known as?", "An embarrassment"),
    ("What European country experienced the highest rate of population decline from 2015 - 2020?", "Lithuania"),
    ("How many bones do we have in an ear?", "3"),
    ("Who famously crossed the Alps with elephants on the way to war with the Romans?", "Hannibal"),
    ("True or False: Halloween originated as an ancient Irish festival.", "True"),
    ("What Netflix show had the most streaming views in 2021?", "Squid Game"),
    ("Which Grammy-nominated New York rapper died in April of 2021?", "DMX"),
    ("What software company is headquartered in Redmond, Washington?", "Microsoft"),
    ("What is the largest Spanish-speaking city in the world?", "Mexico City"),
    ("What is the world's fastest bird?", "The Peregrine Falcon"),
    ("In what country is the Chernobyl nuclear plant located?", "Ukraine"),
    ("The Parthenon Marbles are controversially located in what museum?", "The British Museum")
    # Add more questions and answers here...
]

# Initialize the quiz variables
score = 0
current_question = 0
timer = None
remaining_time = 15

# Create a Tkinter window
window = tk.Tk()
window.title("General Knowledge Quiz")
window.geometry("750x750") # Set the window size to 750x750 pixels
window.configure(bg="black")  # Set the background color to black

# Function to check the answer
def check_answer():
    global score, current_question, timer, remaining_time

    # Retrieve the answer from the entry field
    user_answer = answer_entry.get()

    # Check if the answer is correct
    if user_answer.lower() == quiz_data[current_question][1].lower():
        # Update the score and show "Correct" message
        score += 1
        messagebox.showinfo("Result", "Correct!", icon="info")
    else:
        # Show "Incorrect" message
        messagebox.showerror("Result", "Incorrect!", icon="error")

    # Clear the entry field
    answer_entry.delete(0, tk.END)

    # Show the next question ...
    current_question += 1
    if current_question < len(quiz_data):
        show_question(current_question)
        start_timer()
    else:
        show_result()

# Function to show the next question
def show_question(question_index):
    question_label.config(text=quiz_data[question_index][0])
    answer_entry.delete(0, tk.END)

# Function to show the final result
def show_result():
    messagebox.showinfo("Quiz Result", f"You got {score} questions correct!\n\nScore: {(score / len(quiz_data)) * 100}%")

# Function to handle the timer expiration
def timer_expired():
    messagebox.showinfo("Time's Up!", "Oops! Time's up. Next question!")
    check_answer()

# Function to start the timer
def start_timer():
    global timer, remaining_time
    remaining_time = 10
    timer = window.after(1000, update_timer)

# Function to update the timer label
def update_timer():
    global remaining_time
    remaining_time -= 1
    timer_label.config(text=f"Time: {remaining_time}s")
    if remaining_time >= 0:
        timer = window.after(1000, update_timer)
    else:
        timer_expired()

# Create a frame to hold the question and answer elements
frame = tk.Frame(window, bg="black")
frame.pack(pady=50)

# Create a label for the question
question_label = tk.Label(frame, text="", wraplength=400, font=("Arial", 12), fg="white", bg="black")
question_label.pack()

# Create an entry field for the answer
answer_entry = tk.Entry(frame, font=("Arial", 12))
answer_entry.pack(pady=10)

# Bind the Enter key to the answer entry field
answer_entry.bind("<Return>", lambda event: check_answer())

# Create a rectangular button to submit the answer
submit_button = tk.Button(window, text="Submit", command=check_answer, font=("Arial", 12), bg="black", fg="lime green", relief="flat", width=10, height=2)
submit_button.pack(pady=10)

# Create a label to display the score
score_label = tk.Label(window, text="Score: 0", font=("Arial", 12), fg="white", bg="black")
score_label.place(x=400, y=10, anchor="ne")

# Create a label to display the timer
timer_label = tk.Label(window, text="Time: 15s", font=("Arial", 12), fg="white", bg="black")
timer_label.place(x=10, y=10, anchor="nw")

# Show the first question
show_question(current_question)
start_timer()

# Run the Tkinter event loop
window.mainloop()