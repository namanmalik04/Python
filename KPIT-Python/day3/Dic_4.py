# Initialize an empty dictionary to store battery cells
battery_cells = {}

def add_battery_cell(cell_id, vt, cp, tp):
    """
    Add a new battery cell to the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float): Voltage of the battery cell.
        capacity (float): Capacity of the battery cell.
        temperature (float): Temperature of the battery cell.
    """
    # Create a new dictionary with battery cell information
    cell = {
        "voltage": vt,
        "capacity": cp,
        "temperature": tp
    }
    # Add the battery cell to the dictionary
    battery_cells[cell_id] = cell
    print(f"Battery cell with ID {cell_id} added successfully")

def remove_battery_cell(cell_id):
    """
    Remove a battery cell from the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Remove the battery cell from the dictionary
        del battery_cells[cell_id]
        print(f"Battery cell with ID {cell_id} removed successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def update_battery_cell(cell_id, voltage=None, capacity=None, temperature=None):
    """
    Update a battery cell's information in the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float, optional): Voltage of the battery cell. Defaults to None.
        capacity (float, optional): Capacity of the battery cell. Defaults to None.
        temperature (float, optional): Temperature of the battery cell. Defaults to None.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Update the battery cell information
        if voltage:
            battery_cells[cell_id]["voltage"] = voltage
        if capacity:
            battery_cells[cell_id]["capacity"] = capacity
        if temperature:
            battery_cells[cell_id]["temperature"] = temperature
        print(f"Battery cell with ID {cell_id} updated successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def display_battery_cells():
    """
    Display all battery cells in the dictionary.
    """
    # Check if the dictionary is empty
    if not battery_cells:
        print("No battery cells in the database")
    else:
        # Print each battery cell in the dictionary
        for cell_id, cell in battery_cells.items():
            print(f"Battery Cell ID: {cell_id}")
            print(f"Voltage: {cell['voltage']}")
            print(f"Capacity: {cell['capacity']}")
            print(f"Temperature: {cell['temperature']}")
            print("------------------------")

def search_battery_cell(cell_id):
    """
    Search for a battery cell by ID.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Print the battery cell information
        cell = battery_cells[cell_id]
        print(f"Battery Cell ID: {cell_id}")
        print(f"Voltage: {cell['voltage']}")
        print(f"Capacity: {cell['capacity']}")
        print(f"Temperature: {cell['temperature']}")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def calculate_total_capacity():
    """
    Calculate the total capacity of all battery cells.
    """
  

# Test the functions
add_battery_cell("C1", 3.7, 2000, 25)
add_battery_cell("C2", 3.8, 2500, 30)
add_battery_cell("C3", 3.9, 3000, 35)
print(battery_cells)
display_battery_cells()
search_battery_cell("C1")
calculate_total_capacity()

{"c1":{3.7,2000,25} , }
 