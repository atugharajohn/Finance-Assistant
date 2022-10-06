import tkinter as tk
from tkinter import messagebox
import csv
from tkcalendar import DateEntry

def Seasonal_Fluctuations_form():
    window = tk.Tk()
    window.title("Seasonal Fluctuations Form")

    ID_label = tk.Label(window, text="Infection/disease:")
    ID_label.pack()
    ID_entry = tk.Entry(window)
    ID_entry.pack()

    name_label = tk.Label(window, text="Type:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    Seasonal_label = tk.Label(window, text="Seasonal driver:")
    Seasonal_label.pack()
    Seasonal_entry = tk.Entry(window)
    Seasonal_entry.pack()

    def submit_form():
        student_ID = ID_entry.get()  
        student_name = name_entry.get()
        Seasonal = Seasonal_entry.get()
        
        if not student_ID or not student_name or not Seasonal:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            with open('data\\Seasonal_Fluctuationsdata.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([student_ID, student_name, Seasonal])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        messagebox.showinfo("Success", "Seasonal Fluctuations data saved successfully.")

        ID_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        Seasonal_entry.delete(0, tk.END)

    submit_button = tk.Button(window, text="Submit", command=submit_form)
    submit_button.pack()

    print("\n\nNext Click PREPROCESSING Button...")
def main():
    Seasonal_Fluctuations_form()
