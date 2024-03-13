import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from regression import apply_regression
from extract_data import extract_data

def calculate_sales_quantity():
    target_date = target_date_entry.get()
    material_code = material_code_entry.get()
    sales_office_id = sales_office_id_entry.get()

    try:
        future_data = extract_data(target_date)
        sales_quantity = apply_regression(target_date, material_code, sales_office_id, future_data)
        result_label.config(text=f"Predicted Sales Quantity: {sales_quantity}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Curd Prophet")

# Set window state to zoomed
root.state('zoomed')

# Set font size and family for labels and inputs
font_style = ('sans-serif', 18)

# Create a frame for the header and logo
header_frame = tk.Frame(root, bg="yellow")
header_frame.pack(fill='x')

# Load the logo image
logo_image = Image.open("logo.png")
logo_photo = ImageTk.PhotoImage(logo_image)

# Create and place the logo label
logo_label = tk.Label(header_frame, image=logo_photo, bg="yellow")
logo_label.image = logo_photo  # Keep a reference to the image to prevent garbage collection
logo_label.pack(side=tk.LEFT, padx=10)

# Header with yellow background color
header_label = tk.Label(header_frame, text="Curd Prophet", font=('sans-serif', 24, 'bold'), bg="yellow")
header_label.pack(side=tk.LEFT, fill='y')

# Create input fields
target_date_label = tk.Label(root, text="Target Date:", font=font_style)
target_date_label.pack()
target_date_entry = tk.Entry(root, font=font_style)
target_date_entry.pack()

material_code_label = tk.Label(root, text="Material Code:", font=font_style)
material_code_label.pack()
material_code_entry = tk.Entry(root, font=font_style)
material_code_entry.pack()

sales_office_id_label = tk.Label(root, text="Sales Office ID:", font=font_style)
sales_office_id_label.pack()
sales_office_id_entry = tk.Entry(root, font=font_style)
sales_office_id_entry.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_sales_quantity, font=font_style)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="", font=font_style)
result_label.pack()

# Run the application
root.mainloop()
