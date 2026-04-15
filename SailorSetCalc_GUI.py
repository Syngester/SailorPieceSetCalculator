import tkinter as tk
from tkinter import ttk, messagebox
from SailorSetCalc import (
    EsDeath, Kokushibo, Atomic, ShadowMonarch, Shadow, Ichigo, Ragna, Yamato,
    TrueAizen, Aizen, Rimuru, StrongestShinobi, SaberAlter, BlessedMaiden,
    Anos, Gilgamesh, Madoka, StrongestInHistory, StrongestOfToday, Alucard,
    Yuji, QinShi, Sukuna, Gojo
)

class SailorSetCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sailor Piece Set Calculator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Store references to input widgets
        self.input_widgets = {}
        self.special_widgets = {}  # For yes/no dependent widgets
        
        # Set configurations for each option
        self.set_configs = {
            1: {
                "name": "Esdeath",
                "inputs": ["Ice Core", "Frozen Brand", "Glacier Remnant", "Battle Shard", "Frost Relic"],
                "function": EsDeath,
                "returns_dual": True
            },
            2: {
                "name": "Kokushibo",
                "inputs": ["Moon Crest", "Crescent Shard", "Lunar Essence", "Demon Remnant", "Upper Seal"],
                "function": Kokushibo,
                "returns_dual": True
            },
            3: {
                "name": "Atomic",
                "inputs": ["Atomic Omen", "Eminence Essence", "Shadow Remnant", "Magic Shard", "Abyss Sigil"],
                "function": Atomic,
                "returns_dual": False
            },
            4: {
                "name": "ShadowMonarch",
                "inputs": ["Monarch Core", "Monarch Essence", "Kamish Dagger", "Shadow Crystal"],
                "function": ShadowMonarch,
                "returns_dual": False
            },
            5: {
                "name": "Shadow",
                "inputs": ["Atomic Core", "Shadow Essence", "Void Seed", "Umbral Capsule"],
                "function": Shadow,
                "returns_dual": False
            },
            6: {
                "name": "Ichigo",
                "inputs": ["Soul Flame", "Spiritual Core", "Soul Fragment"],
                "function": Ichigo,
                "returns_dual": False
            },
            7: {
                "name": "Ragna",
                "inputs": ["Wyrm Brand", "Black Frost", "Silver Requiem"],
                "function": Ragna,
                "returns_dual": False
            },
            8: {
                "name": "Yamato",
                "inputs": ["Azure Heart", "Silent Storm", "Yamato Essence", "Frozen Will"],
                "function": Yamato,
                "returns_dual": False
            },
            9: {
                "name": "TrueAizen",
                "inputs": ["Evolution Fragment", "Transcendent Core", "Divinity Essence", "Fusion Ring", "Chrysalis Sigil"],
                "function": TrueAizen,
                "returns_dual": False
            },
            10: {
                "name": "Aizen",
                "inputs": ["Mirage Pendants", "Illusion Prisms", "Reiatsu Core", "Hogyoku Fragment"],
                "function": Aizen,
                "returns_dual": False
            },
            11: {
                "name": "Rimuru",
                "inputs": ["Sage Pulse", "Tempest Seal", "Slime Remnant", "Slime Core"],
                "function": Rimuru,
                "returns_dual": False
            },
            12: {
                "name": "StrongestShinobi",
                "inputs": ["Path Fragment", "Eternal Core", "Battle Sigil", "Power Remnant"],
                "function": StrongestShinobi,
                "returns_dual": True
            },
            13: {
                "name": "SaberAlter",
                "inputs": ["Dark Grail", "Morgan Remnant", "Alter Essence", "Corruption Core", "Corrupt Crown"],
                "function": SaberAlter,
                "returns_dual": True
            },
            14: {
                "name": "BlessedMaiden",
                "inputs": ["Celestial Mark", "Aero Core", "Gale Essence", "Tide Remnant", "Tempest Relic"],
                "function": BlessedMaiden,
                "returns_dual": True
            },
            15: {
                "name": "Anos",
                "inputs": ["Calamity Seal", "Demonic Fragment", "Demonic Shard", "Destruction Eye", "Imperial Mark"],
                "function": Anos,
                "returns_dual": False
            },
            16: {
                "name": "Gilgamesh",
                "inputs": ["Throne Remnant", "Ancient Shard", "Golden Essence", "Phantasm Core", "Broken Sword"],
                "function": Gilgamesh,
                "returns_dual": True
            },
            17: {
                "name": "Madoka",
                "inputs": ["Heart", "Divine Fragment", "Sacred Bow", "Radiant Core", "Pink Gem"],
                "function": Madoka,
                "returns_dual": False
            },
            18: {
                "name": "StrongestInHistory",
                "inputs": ["Cursed Flesh", "Malevolent Soul", "Vessel Ring"],
                "special_inputs": {
                    "Y": ["Awakened Cursed Fingers", "Cursed Talisman", "Infinity Essence"],
                    "N": []
                },
                "function": StrongestInHistory,
                "returns_dual": True,
                "has_consumable": True
            },
            19: {
                "name": "StrongestOfToday",
                "inputs": ["Infinity Essence", "Blue Singularity", "Reversal Pulse"],
                "special_inputs": {
                    "Y": ["Six Eyes", "Energy Shards", "Cursed Flesh"],
                    "N": []
                },
                "function": StrongestOfToday,
                "returns_dual": True,
                "has_consumable": True
            },
            20: {
                "name": "Alucard",
                "inputs": ["Blood Ring", "Casull", "Soul Amulet"],
                "function": Alucard,
                "returns_dual": False
            },
            21: {
                "name": "Yuji",
                "inputs": ["Divergent Pulse", "Flash Impact", "Energy Core"],
                "function": Yuji,
                "returns_dual": False
            },
            22: {
                "name": "QinShi",
                "inputs": ["Imperial Seal", "Jade Tablet"],
                "function": QinShi,
                "returns_dual": False
            },
            23: {
                "name": "Sukuna",
                "inputs": ["Cursed Finger", "Dismantle Fang", "Crimson Heart"],
                "function": Sukuna,
                "returns_dual": False
            },
            24: {
                "name": "Gojo",
                "inputs": ["Void Fragment", "Limitless Ring", "Infinity Core"],
                "function": Gojo,
                "returns_dual": False
            }
        }
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Sailor Piece Set Calculator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Set selection
        select_frame = ttk.Frame(self.root)
        select_frame.pack(padx=10, pady=5, fill=tk.X)
        
        ttk.Label(select_frame, text="Select Set:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.set_var = tk.StringVar()
        set_options = [f"{i}. {self.set_configs[i]['name']}" for i in range(1, 25)]
        
        set_menu = ttk.Combobox(select_frame, textvariable=self.set_var, values=set_options, state="readonly", width=30)
        set_menu.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        set_menu.bind("<<ComboboxSelected>>", self.on_set_selected)
        
        # Input frame (scrollable)
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Result frame
        result_frame = ttk.LabelFrame(self.root, text="Result", padding=10)
        result_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.result_label = tk.Label(result_frame, text="Select a set and fill in the values", font=("Arial", 10), fg="green")
        self.result_label.pack()
        
        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=10, fill=tk.X)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_inputs).pack(side=tk.LEFT, padx=5)
        
    def on_set_selected(self, event=None):
        # Clear previous inputs
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.input_widgets.clear()
        self.special_widgets.clear()
        
        selected = self.set_var.get()
        if not selected:
            return
        
        set_num = int(selected.split(".")[0])
        config = self.set_configs[set_num]
        
        # Create input fields
        for i, input_name in enumerate(config["inputs"]):
            frame = ttk.Frame(self.input_frame)
            frame.pack(padx=5, pady=5, fill=tk.X)
            
            label = ttk.Label(frame, text=f"{input_name}:", width=25)
            label.pack(side=tk.LEFT, padx=5)
            
            entry = ttk.Entry(frame, width=15)
            entry.pack(side=tk.LEFT, padx=5)
            self.input_widgets[input_name] = entry
        
        # Handle special yes/no inputs
        if config.get("has_consumable"):
            # Add consumable yes/no selection
            frame = ttk.Frame(self.input_frame)
            frame.pack(padx=5, pady=5, fill=tk.X)
            
            label = ttk.Label(frame, text="Consumables?", width=25)
            label.pack(side=tk.LEFT, padx=5)
            
            self.consumable_var = tk.StringVar(value="N")
            ttk.Radiobutton(frame, text="Yes", variable=self.consumable_var, value="Y", command=self.on_consumable_changed).pack(side=tk.LEFT, padx=5)
            ttk.Radiobutton(frame, text="No", variable=self.consumable_var, value="N", command=self.on_consumable_changed).pack(side=tk.LEFT, padx=5)
            
            # Create frames for special inputs (initially hidden)
            self.special_frame = ttk.Frame(self.input_frame)
            self.special_frame.pack(padx=5, pady=5, fill=tk.X)
            
            self.display_special_inputs(set_num, "N")
    
    def on_consumable_changed(self):
        selected = self.set_var.get()
        if not selected:
            return
        
        set_num = int(selected.split(".")[0])
        choice = self.consumable_var.get()
        self.display_special_inputs(set_num, choice)
    
    def display_special_inputs(self, set_num, choice):
        # Clear previous special widgets
        for widget in self.special_frame.winfo_children():
            widget.destroy()
        self.special_widgets.clear()
        
        config = self.set_configs[set_num]
        special_inputs = config.get("special_inputs", {}).get(choice, [])
        
        for input_name in special_inputs:
            frame = ttk.Frame(self.special_frame)
            frame.pack(padx=5, pady=5, fill=tk.X)
            
            label = ttk.Label(frame, text=f"{input_name}:", width=25)
            label.pack(side=tk.LEFT, padx=5)
            
            entry = ttk.Entry(frame, width=15)
            entry.pack(side=tk.LEFT, padx=5)
            self.special_widgets[input_name] = entry
    
    def calculate(self):
        selected = self.set_var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select a set first")
            return
        
        set_num = int(selected.split(".")[0])
        config = self.set_configs[set_num]
        
        try:
            # Collect input values
            values = {}
            for input_name, entry in self.input_widgets.items():
                value = entry.get()
                if not value:
                    messagebox.showerror("Error", f"Please enter {input_name}")
                    return
                values[input_name] = int(value)
            
            # Collect special input values if needed
            for input_name, entry in self.special_widgets.items():
                value = entry.get()
                if not value:
                    messagebox.showerror("Error", f"Please enter {input_name}")
                    return
                values[input_name] = int(value)
            
            # Call the appropriate function
            if config.get("has_consumable"):
                consumable_choice = self.consumable_var.get()
                result = self.call_consumable_function(config["function"], consumable_choice, values, config)
            else:
                result = config["function"](*values.values())
            
            # Display result
            if config["returns_dual"]:
                sets, setsF = result
                self.result_label.config(text=f"{sets} {config['name']} sets and {setsF} with F moves", fg="green")
            else:
                self.result_label.config(text=f"{result} {config['name']} sets", fg="green")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def call_consumable_function(self, function, choice, values, config):
        # Reorganize values for consumable functions
        if config['name'] == "StrongestInHistory":
            values_list = [
                choice,
                values.get("Cursed Flesh", 0),
                values.get("Malevolent Soul", 0),
                values.get("Vessel Ring", 0),
                values.get("Awakened Cursed Fingers", 0),
                values.get("Cursed Talisman", 0),
                values.get("Infinity Essence", 0)
            ]
        elif config['name'] == "StrongestOfToday":
            values_list = [
                choice,
                values.get("Infinity Essence", 0),
                values.get("Blue Singularity", 0),
                values.get("Reversal Pulse", 0),
                values.get("Six Eyes", 0),
                values.get("Energy Shards", 0),
                values.get("Cursed Flesh", 0)
            ]
        
        return function(*values_list)
    
    def clear_inputs(self):
        for entry in self.input_widgets.values():
            entry.delete(0, tk.END)
        for entry in self.special_widgets.values():
            entry.delete(0, tk.END)
        self.result_label.config(text="Select a set and fill in the values")

if __name__ == "__main__":
    root = tk.Tk()
    app = SailorSetCalculatorGUI(root)
    root.mainloop()
