import tkinter as tk
import pytz
from datetime import datetime

# Get a list of all available time zones
time_zones = pytz.all_timezones

# Create the main window
window = tk.Tk()
window.title("Time Zone Converter")

# Create a label for the input time zone
input_label = tk.Label(window, text="Input Time Zone:")
input_label.pack()

# Create a dropdown menu for the input time zone
input_variable = tk.StringVar(window)
input_variable.set(time_zones[0])
input_menu = tk.OptionMenu(window, input_variable, *time_zones)
input_menu.pack()

# Create a label for the output time zone
output_label = tk.Label(window, text="Output Time Zone:")
output_label.pack()

# Create a dropdown menu for the output time zone
output_variable = tk.StringVar(window)
output_variable.set(time_zones[0])
output_menu = tk.OptionMenu(window, output_variable, *time_zones)
output_menu.pack()

# Create a label for the input time
time_label = tk.Label(window, text="Input Time:")
time_label.pack()

# Create an entry field for the input time
time_entry = tk.Entry(window)
time_entry.pack()

# Create a function to convert the time
def convert_time():
    # Get the input time zone and time
    tz_input = pytz.timezone(input_variable.get())
    time_input = datetime.strptime(time_entry.get(), "%Y-%m-%d %H:%M:%S")

    # Convert the time to the desired time zone
    tz_output = pytz.timezone(output_variable.get())
    time_output = tz_input.localize(time_input).astimezone(tz_output)

    # Update the output label with the converted time
    output_label.config(text=f"Output Time: {time_output}")

# Create a button to convert the time
convert_button = tk.Button(window, text="Convert Time", command=convert_time)
convert_button.pack()

# Run the main loop
window.mainloop()