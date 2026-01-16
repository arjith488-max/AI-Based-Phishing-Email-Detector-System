import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model
model = joblib.load("phishing_model.pkl")

# Function to check email
def check_email():
    email_text = text_box.get("1.0", tk.END).strip()

    if email_text == "":
        messagebox.showwarning("Input Error", "Please enter email content")
        return

    result = model.predict([email_text])

    if result[0] == "phishing":
        result_label.config(text="⚠ PHISHING EMAIL DETECTED", fg="red")
    else:
        result_label.config(text="✔ SAFE EMAIL", fg="green")

# Main window
root = tk.Tk()
root.title("AI Phishing Email Detector")
root.geometry("600x420")
root.configure(bg="#1e1e1e")

# Title
title_label = tk.Label(
    root,
    text="AI-Based Phishing Email Detector",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title_label.pack(pady=20)

# Text input box
text_box = tk.Text(root, height=8, width=60, font=("Arial", 12))
text_box.pack(pady=10)

# Check button
check_button = tk.Button(
    root,
    text="Check Email",
    font=("Arial", 14),
    bg="blue",
    fg="white",
    command=check_email
)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e"
)
result_label.pack(pady=20)

# Run app
root.mainloop()
