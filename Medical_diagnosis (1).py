# Python Library for GUI (graphical user interface) - Tkinter
import tkinter as tk

# Python Library more modern for Adding Message Box in Tkinter (Check Box ,styled buttons, etc) - messagebox
from tkinter import ttk

# Function to diagnose based on selected symptoms 
# That takes one argument (symptoms) which is a list of symptoms selected by the user and returns a diagnosis based on the symptoms provided.
def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms and "fatigue" in symptoms:
        return "COVID-19"
    elif "fever" in symptoms and "cough" in symptoms and "body_ache" in symptoms:
        return "Flu"
    elif "cough" in symptoms and "sneezing" in symptoms and "runny_nose" in symptoms:
        return "Common Cold"
    elif "sneezing" in symptoms and "runny_nose" in symptoms and "itchy_eyes" in symptoms:
        return "Allergy"
    elif "nausea" in symptoms and "vomiting" in symptoms:
        return "Food Poisoning"
    elif "cough" in symptoms and "fatigue" in symptoms and "chest_pain" in symptoms:
        return "Bronchitis"
    elif "chest_pain" in symptoms and "shortness_of_breath" in symptoms:
        return "Pneumonia"
    elif "fatigue" in symptoms and "blurred_vision" in symptoms:
        return "Diabetes"
    elif "headache" in symptoms and "dizziness" in symptoms:
        return "Hypertension"
    else:
        return "Symptoms not recognized, please consult a doctor"
    
# Function to get selected symptoms from btn 
# check from checkboxes and call the diagnose function to get the diagnosis based on the selected symptoms, then update the result_label with the diagnosis.
def get_diagnosis():
    selected = []
    for symptom, var in symptom_vars.items():
        if var.get():
            selected.append(symptom)
    result = diagnose(selected)
    result_label.config(text="Diagnosis: " + result)
# This part responsible for creating the main application window, setting its title, size, and background color. It also configures the styles for the checkboxes and buttons, creates a title label, a frame to hold the checkboxes, and a button to trigger the diagnosis. Finally, it starts the main event loop to run the application.
root = tk.Tk()
root.title("Medical Symptom Checker")
root.geometry("600x600")
root.configure(bg="#e8ecf1")

style = ttk.Style()
style.theme_use("clam")
# Configure the style for checkboxes and buttons to have a consistent look and feel, including background color, foreground color, font, and padding. The map method is used to change the background color of checkboxes when they are active (hovered over).
style.configure("TCheckbutton",
                background="#e8ecf1",
                foreground="#333",
                font=("Arial", 10),
                padding=3)

# This line changes the background color of checkboxes to a lighter shade when they are active (hovered over) to provide visual feedback to the user.
style.map("TCheckbutton",
        background=[("active", "#dfe4ea")])

# Configure the style for buttons to have a consistent look and feel, including font and padding.
style.configure("TButton",
                font=("Arial", 10),
                padding=6)

# Create a title label at the top of the application window with the text "Medical Symptom Checker", using a bold Arial font, and set its background and foreground colors to match the overall theme of the application. The label is then packed with some vertical padding to create space around it.
title_label = tk.Label(root,
                    text="Medical Symptom Checker",
                    font=("Arial", 15, "bold"),
                    bg="#e8ecf1",
                    fg="#2c3e50")
title_label.pack(pady=12)

# Create a frame to hold the checkboxes for the symptoms, set its background color to match the overall theme of the application, and pack it to fill the available space in the main window.
frame = tk.Frame(root, bg="#e8ecf1")
frame.pack()

symptoms_list = [
    "fever", "cough", "fatigue", "body_ache", "sneezing",
    "runny_nose", "itchy_eyes", "nausea", "vomiting",
    "chest_pain", "shortness_of_breath", "blurred_vision",
    "headache", "dizziness"
]

# Stor the symptom var in a disctionary 
symptom_vars = {}

# Loop through the symptoms list and create a checkbox for each symptom, storing the associated BooleanVar in the symptom_vars dictionary for later retrieval when checking which symptoms are selected.
for symptom in symptoms_list:
    var = tk.BooleanVar()
    chk = ttk.Checkbutton(frame, text=symptom, variable=var)
    chk.pack(anchor='w', padx=15, pady=3)
    symptom_vars[symptom] = var

check_btn = ttk.Button(root, text="Check Diagnosis", command=get_diagnosis)
check_btn.pack(pady=12)

result_label = tk.Label(root,
                        text="Diagnosis: ",
                        font=("Arial", 11),
                        bg="#e8ecf1",
                        fg="#2c3e50")
result_label.pack(pady=10)
# Start the main event loop to run the application, allowing the user to interact with the GUI and trigger events such as button clicks.
root.mainloop()