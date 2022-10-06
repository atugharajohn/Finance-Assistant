import tkinter as tk
from tkinter import messagebox
import csv
from tkcalendar import DateEntry
import Data2

def Disease_Patterns_form():
    window = tk.Tk()
    window.title("Disease Patterns Form")

    ID_label = tk.Label(window, text="Disease ID:")
    ID_label.pack()
    ID_entry = tk.Entry(window)
    ID_entry.pack()

    name_label = tk.Label(window, text="Disease Name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    subject_label = tk.Label(window, text="Description:")
    subject_label.pack()
    subject_entry = tk.Entry(window)
    subject_entry.pack()

    def submit_form():
        patient_ID = ID_entry.get()  
        patient_name = name_entry.get()
        subject = subject_entry.get()

        if not patient_ID or not patient_name or not subject:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            with open('data\\Disease_Patternsdata.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([patient_ID, patient_name, subject])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        messagebox.showinfo("Success", "Disease Patterns data saved successfully.")

        ID_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)

    submit_button = tk.Button(window, text="Submit", command=submit_form)
    submit_button.pack()
    Data2.main()
    window.mainloop()

def main():
    Disease_Patterns_form()
