import tkinter as tk
import requests


# Function to get the age from the API
def getAge():
    name = name_entry.get()
    if name:
        try:
            response = requests.get(f"https://api.agify.io/?name={name}")
            data = response.json()
            age_label.config(text=f"Estimated Age: {data['age']} years.")
        except Exception as e:
            age_label.config(text="Error getting age.")
    else:
        age_label.config(text="Please enter a name.")


# Main window config
root = tk.Tk()
root.title("Age Estimator App")
root.geometry("300x450")
root.configure(bg="#0D1B2A")

# Frame for the content
content_frame = tk.Frame(root, bg="#0D1B2A")
content_frame.pack(expand=True, fill="both", padx=20, pady=20)

# App name label
app_name_label = tk.Label(
    content_frame,
    text="Age Estimator",
    bg="#1B263B",
    fg="#E0E1DD",
    font=("Helvetica", 16),
)
app_name_label.pack(fill="x", padx=10, pady=(10, 20))

# Divider
divider = tk.Frame(content_frame, height=2, bg="#000000")
divider.pack(fill="x")

# Name input field
name_label = tk.Label(
    content_frame, text="Enter your first name:", bg="#1B263B", fg="#E0E1DD"
)
name_label.pack(fill="x", padx=10, pady=(20, 10))
name_entry = tk.Entry(content_frame, bg="#E0E1DD")
name_entry.pack(fill="x", padx=10, pady=10)

# Age display label
age_label = tk.Label(
    content_frame, text="", bg="#1B263B", fg="#E0E1DD", font=("Helvetica", 14)
)
age_label.pack(fill="x", padx=10, pady=(10, 20))

# Get Age button
get_age_button = tk.Button(
    content_frame,
    text="Get Age",
    bg="#415A77",
    fg="#E0E1DD",
    font=("Helvetica", 12),
    command=getAge,
)
get_age_button.pack(fill="x", padx=10, pady=(0, 20))

# Run the Tkinter main loop
root.mainloop()