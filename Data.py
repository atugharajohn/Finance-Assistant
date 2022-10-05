import tkinter as tk
from tkinter import messagebox
import csv
from tkcalendar import DateEntry
import Data1
def Patient_Demographics_form():
    window = tk.Tk()
    window.title("Patient Demographics Form")

    ID_label = tk.Label(window, text="Patient ID:")
    ID_label.pack()
    ID_entry = tk.Entry(window)
    ID_entry.pack()

    name_label = tk.Label(window, text="Patient Name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    date_label = tk.Label(window, text="Date:")
    date_label.pack()
    date_entry = DateEntry(window)
    date_entry.pack()

    address_label = tk.Label(window, text="Address:")
    address_label.pack()
    address_entry = tk.Entry(window)
    address_entry.pack()

    def submit_form():
        patient_ID = ID_entry.get() 
        patient_name = name_entry.get()
        date = date_entry.get()
        address = address_entry.get()

        if not patient_ID or not patient_name or not date or not address:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            with open('data\\patient_addressdata.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([patient_ID, patient_name, date, address])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        messagebox.showinfo("Success", "patient address data saved successfully.")

        ID_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

    submit_button = tk.Button(window, text="Submit", command=submit_form)
    submit_button.pack()
    Data1.main()
    window.mainloop()

def main():
    Patient_Demographics_form()
    
