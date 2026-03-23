#refactored the converter.py program into a visual gui
import tkinter as tk
from tkinter import ttk

#conversion dictionary
#length - using meter as base
TO_METERS = {
    "km": {"name":"Kilometer" ,"factor":1000},
    "mi": {"name":"Mile" ,"factor":1609.34},
    "m": {"name":"Meter" ,"factor":1},
    "ft": {"name":"Feet" ,"factor":0.3048},
    "in": {"name":"Inch" ,"factor":0.0254},
    "cm": {"name":"Centimeter" ,"factor":0.01},
    "mm": {"name":"Milimeter" ,"factor":0.001}
}
#weight - using gram as base
TO_GRAMS = {
    "t": {"name":"Metric ton" ,"factor":1000000},
    "kg": {"name":"Kilogram" ,"factor":1000},
    "lb": {"name":"Pound" ,"factor":453.59},
    "oz": {"name":"Ounce" ,"factor":28.34},
    "g": {"name":"Gram" ,"factor":1},
    "ct": {"name":"Carat" ,"factor":0.2},
    "mg": {"name":"Miligram" ,"factor":0.001}
}
#volume - using liter as base
TO_LITERS = {
    "osp": {"name":"Olympic Swimming Pool" ,"factor":2500000},
    "m3": {"name":"Cubic Meter" ,"factor":1000},
    "bbl": {"name":"Barrel" ,"factor":159},
    "ft3": {"name":"Cubic foot" ,"factor":28.31},
    "l": {"name":"Liter" ,"factor":1},
    "gal": {"name":"Gallon" ,"factor":4.54},
    "ml": {"name":"Mililiter" ,"factor":0.001}
}
#dictionary just for the dropdown names
VALID_TEMPS = {
    "c": {"name":"Celsius"},
    "f": {"name":"Fahrenheit"},
    "k": {"name":"Kelvin"}
}

#temperature
#since temperature conversion isn't linear, we can't do the same as the others
def to_celsius(value, unit):
    if unit == "c":
        return value
    elif unit == "f":
        return (value - 32) * 5/9
    elif unit == "k":
        return value - 273.15

def from_celsius(value, unit):
    if unit == "c":
        return value
    elif unit == "f":
        return (value * 9/5) + 32
    elif unit == "k":
        return value + 273.15

#outputs the result the same way the normal conversion does, but the calculation isn't done here
def convert_temperature(value, from_unit, to_unit, conversion_table=None):
    return from_celsius(to_celsius(value, from_unit), to_unit)

def convert(value, from_unit, to_unit, conversion_table):
    base = value * conversion_table[from_unit]["factor"]
    return base / conversion_table[to_unit]["factor"]

#since the dropdowns display the name, this gets the abbreviation, which is used to find the factor to be used
def get_abbrev(name, conversion_table):
    for abbrev, info in conversion_table.items():
        if info["name"] == name:
            return abbrev

#nothing is calculated on the calculate function either
#handles changing the label to the answer and also adding the last calculation to the history
def calculate(value, from_unit, to_unit, conversion_table, use_func, result_var):
    from_abbrev = get_abbrev(from_unit.get(), conversion_table)
    to_abbrev = get_abbrev(to_unit.get(), conversion_table)
    output = use_func(float(value.get()), from_abbrev, to_abbrev, conversion_table)
    entry = f"{value.get()} {from_abbrev} = {round(output, 2)} {to_abbrev}"
    result_var.set(entry)
    last = history_box.get(tk.END)
    if entry != last:
        history_box.insert(tk.END, entry)

    

# converting the tab name into an existing dictionary for the dropdowns and calculation
TAB_LOOKUP = {
    "Length":      {"table": TO_METERS,    "func": convert},
    "Weight":      {"table": TO_GRAMS, "func": convert},
    "Volume":      {"table": TO_LITERS,    "func": convert},
    "Temperature": {"table": VALID_TEMPS, "func": convert_temperature},
}

#actually drawing the tab content
def load_tab(event=None):
    active_tab_id = notebook.select()
    active_tab = root.nametowidget(active_tab_id)
    active_tab_text = notebook.tab(active_tab_id, "text")
    tab_data = TAB_LOOKUP[active_tab_text]
    conversion_table = tab_data["table"]
    use_func = tab_data["func"]

    value = tk.StringVar()
    from_unit = tk.StringVar()
    to_unit = tk.StringVar()
    result = tk.StringVar()
    result.set("Input data above")
    
    for widget in active_tab.winfo_children():
        widget.destroy()
    
    tk.Label(active_tab, text="Value:", padx=2, pady=2, anchor="e", width=10).grid(row=0,column=0, pady=2)
    tk.Label(active_tab, text="from:", padx=2, pady=2, anchor="e", width=10).grid(row=1,column=0, pady=2)
    tk.Label(active_tab, text="to:", padx=2, pady=2, anchor="e", width=10).grid(row=2,column=0, pady=2)
    
    tk.Entry(active_tab, width=22, textvariable=value).grid(row=0,column=1)

    from_dropdown = ttk.Combobox(active_tab, width=20,textvariable=from_unit)
    from_dropdown.grid(row=1, column=1)
    from_dropdown["values"] = [info["name"] for info in conversion_table.values()]

    to_dropdown = ttk.Combobox(active_tab, width=20, textvariable=to_unit)
    to_dropdown.grid(row=2, column=1)
    to_dropdown["values"] = [info["name"] for info in conversion_table.values()]

    tk.Button(active_tab, text="Calculate", width=20, padx=10, pady=2, command=lambda: calculate(value, from_unit, to_unit, conversion_table, use_func, result)).grid(row=4, column=1)
    
    tk.Label(active_tab, textvariable=result, anchor="center").grid(row=5, columnspan=2)
    

root = tk.Tk(className="converter")
root.title("Unit Converter")
root.geometry("470x200")

#Left frame:tabs
FrameL = tk.Frame(root, width=320)
FrameL.pack(side="left", fill="y")
FrameL.pack_propagate(0)

#Right frame: history
FrameR = tk.Frame(root)
FrameR.pack(side="right", fill="both", expand=True)
FrameR.pack_propagate(0)

#makes the tabs fill the frame width styles the text
style = ttk.Style()
style.configure('TNotebook.Tab', width=100, anchor="center", font=('Nerd', 8))
notebook = ttk.Notebook(FrameL)
notebook.pack(expand=True, fill="both")

#the tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
notebook.add(tab1, text="Length")
notebook.add(tab2, text="Weight")
notebook.add(tab3, text="Volume")
notebook.add(tab4, text="Temperature")

#Frame for the history label and trash button, easiest way to make it stay above the history listbox
top_bar = tk.Frame(FrameR)
top_bar.pack(fill="x")
tk.Label(top_bar, text="History", font=('Nerd', 8), pady=2).pack(side="left")
tk.Button(top_bar, text="🗑", bg="red", fg="white", font=('Nerd', 9), padx=0, pady=0, command=lambda: history_box.delete(0, tk.END)).pack(side="right")

#history listbox, fills up the rest of the space in the frame.
history_box = tk.Listbox(FrameR, takefocus=0, bg="lightgray", font=('Nerd', 10))
history_box.pack(fill="both", expand=True)

#loads the tab when the app first starts
notebook.bind("<<NotebookTabChanged>>", load_tab)
root.mainloop()