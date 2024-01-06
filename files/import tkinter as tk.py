import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Dynamic Form Example")

# Function to update variables fields
def update_variables_fields(aspect_frame, var_count):
    # Clear the frame
    for widget in aspect_frame.winfo_children():
        widget.destroy()

    # Add the new variable entries
    for i in range(var_count.get()):
        tk.Entry(aspect_frame, width=50).pack()

# Function to update aspects
def update_aspects(num_aspects, aspects_frame, aspect_var_counts):
    # Clear the aspects frame
    for widget in aspects_frame.winfo_children():
        widget.destroy()

    # Reset the list that keeps track of the number of variables for each aspect
    aspect_var_counts.clear()

    # Add the new aspects with variable fields
    for i in range(num_aspects.get()):
        aspect_label = tk.Label(aspects_frame, text=f"Aspect {i+1}")
        aspect_label.pack()
        
        var_count = tk.IntVar(value=0)
        aspect_var_counts.append(var_count)
        
        var_count_label = tk.Label(aspects_frame, text="Quantas variáveis?")
        var_count_label.pack()

        var_count_entry = tk.Entry(aspects_frame, textvariable=var_count)
        var_count_entry.pack()

        aspect_variables_frame = tk.Frame(aspects_frame)
        aspect_variables_frame.pack()

        # Update the variables whenever the number changes
        var_count.trace("w", lambda *args, frame=aspect_variables_frame, count=var_count: update_variables_fields(frame, count))

# Function to collect and print form data
def submit_form(aspect_var_counts):
    # Here you can process the form data and send it wherever you need
    print(f"Tenant Name: {tenant_name.get()}")
    print(f"Type Name: {type_name.get()}")
    for i, var_count in enumerate(aspect_var_counts, start=1):
        print(f"Aspect {i} has {var_count.get()} variables.")

# Create frames
header_frame = tk.Frame(root)
header_frame.pack()

aspects_frame = tk.Frame(root)
aspects_frame.pack()

footer_frame = tk.Frame(root)
footer_frame.pack()

# Entry for number of aspects
num_aspects = tk.IntVar(value=1)
num_aspects_label = tk.Label(header_frame, text="Quantos Aspects?")
num_aspects_label.pack()

num_aspects_entry = tk.Entry(header_frame, textvariable=num_aspects)
num_aspects_entry.pack()

# Button to update aspects
aspect_var_counts = []
update_button = tk.Button(header_frame, text="Update Aspects", command=lambda: update_aspects(num_aspects, aspects_frame, aspect_var_counts))
update_button.pack()

# Tenant name entry
tenant_name_label = tk.Label(footer_frame, text="Tenant Name")
tenant_name_label.pack()

tenant_name = tk.Entry(footer_frame)
tenant_name.pack()

# Type name entry
type_name_label = tk.Label(footer_frame, text="Type Name")
type_name_label.pack()

type_name = tk.Entry(footer_frame)
type_name.pack()

# Submit button
submit_button = tk.Button(footer_frame, text="Send Model", command=lambda: submit_form(aspect_var_counts))
submit_button.pack()

# Initialize aspects
update_aspects(num_aspects, aspects_frame, aspect_var_counts)

# Start the application
root.mainloop()
