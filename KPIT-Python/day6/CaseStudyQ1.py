'''
Case Study1:
Design a Vehicle Management System that allows users to store, update, and manage records of different types of vehicles. The system should:
Support multiple vehicle types (Car, Truck, Motorcycle) using Enum for type safety.
Allow adding, removing, updating, and retrieving vehicle details.
Track mileage and maintenance history for each vehicle.
Provide filtering capabilities based on vehicle type.
Display all stored vehicle records in a readable format.
Class and Function Details:
1. Enum: VehicleType
Purpose: Defines allowed vehicle types using Python's Enum for type safety.
Values: CAR, TRUCK, MOTORCYCLE
Why Enum? Prevents invalid vehicle type entries and improves code readability.
2. Class: VehicleRecords
This class acts as the core of the system, managing all vehicle-related operations.
Attributes:
self.vehicles: Dictionary to store vehicle records with vehicle_id as key.
self.fuel_types: List of allowed fuel types (Gasoline, Diesel, Electric).
self.transmission_types: List of allowed transmission types (Automatic, Manual).
Functions in VehicleRecords
a) __init__(self)
Purpose: Initializes the vehicle records system.
Details: Creates an empty dictionary for vehicles and sets allowed fuel and transmission types.
b) add_vehicle(self, vehicle_type, make, model, year, fuel_type, transmission_type, mileage=0)
Purpose: Adds a new vehicle to the system.
Steps:
Validate vehicle_type is an instance of VehicleType.
Generate a unique vehicle_id based on current count.
Store vehicle details in self.vehicles dictionary.
Key Features: Initializes maintenance_records as an empty list for future service logs.
c) remove_vehicle(self, vehicle_id)
Purpose: Deletes a vehicle record by its ID.
Behavior: Prints confirmation if removed, else shows "not found".
d) update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None)
Purpose: Updates specific details of a vehicle.
Logic: Checks if vehicle_id exists, then updates only provided fields (partial update supported).
e) get_vehicle_info(self, vehicle_id)
Purpose: Retrieves details of a specific vehicle.
Returns: Dictionary of vehicle info or None if not found.
f) drive_vehicle(self, vehicle_id, miles)
Purpose: Simulates driving the vehicle by adding miles to its mileage.
Validation: Ensures vehicle exists before updating mileage.
g) perform_maintenance(self, vehicle_id, maintenance_type, description)
Purpose: Logs maintenance activity for a vehicle.
Details: Appends a dictionary with maintenance_type and description to maintenance_records.
h) display_all_vehicles(self)
Purpose: Prints all vehicle records in a readable format.
Output: Displays each vehicle's details and maintenance history.
i) filter_vehicles_by_type(self, vehicle_type)
Purpose: Returns a dictionary of vehicles matching the given type.
Validation: Ensures vehicle_type is a valid VehicleType.
 
------------------------------------------------------------------------------------------------------------------
'''


# Solution:


from enum import Enum
# Define Enum for Vehicle Types
class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"
class VehicleRecords:
    def __init__(self):
        self.vehicles = {}
        self.fuel_types = ["Gasoline", "Diesel", "Electric"]
        self.transmission_types = ["Automatic", "Manual"]
    def add_vehicle(self, vehicle_type: VehicleType, make, model, year, fuel_type, transmission_type, mileage=0):
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        vehicle_id = len(self.vehicles) + 1
        self.vehicles[vehicle_id] = {
            "vehicle_type": vehicle_type.value,  # Store the string value
            "make": make,
            "model": model,
            "year": year,
            "fuel_type": fuel_type,
            "transmission_type": transmission_type,
            "mileage": mileage,
            "maintenance_records": []
        }
        print(f"Vehicle added with ID: {vehicle_id}")
    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            print(f"Vehicle with ID {vehicle_id} removed")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")
    def update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None):
        if vehicle_id in self.vehicles:
            if make:
                self.vehicles[vehicle_id]["make"] = make
            if model:
                self.vehicles[vehicle_id]["model"] = model
            if year:
                self.vehicles[vehicle_id]["year"] = year
            if fuel_type:
                self.vehicles[vehicle_id]["fuel_type"] = fuel_type
            if transmission_type:
                self.vehicles[vehicle_id]["transmission_type"] = transmission_type
            if mileage:
                self.vehicles[vehicle_id]["mileage"] = mileage
            print(f"Vehicle with ID {vehicle_id} updated")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")
    def get_vehicle_info(self, vehicle_id):
        return self.vehicles.get(vehicle_id, None)
    def drive_vehicle(self, vehicle_id, miles):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id]["mileage"] += miles
            print(f"Vehicle with ID {vehicle_id} driven for {miles} miles")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")
    def perform_maintenance(self, vehicle_id, maintenance_type, description):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id]["maintenance_records"].append({
                "maintenance_type": maintenance_type,
                "description": description
            })
            print(f"Maintenance performed on Vehicle with ID {vehicle_id}")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")
    def display_all_vehicles(self):
        for vehicle_id, vehicle_info in self.vehicles.items():
            print(f"Vehicle ID: {vehicle_id}")
            print(f"Vehicle Type: {vehicle_info['vehicle_type']}")
            print(f"Make: {vehicle_info['make']}")
            print(f"Model: {vehicle_info['model']}")
            print(f"Year: {vehicle_info['year']}")
            print(f"Fuel Type: {vehicle_info['fuel_type']}")
            print(f"Transmission Type: {vehicle_info['transmission_type']}")
            print(f"Mileage: {vehicle_info['mileage']}")
            print(f"Maintenance Records: {vehicle_info['maintenance_records']}")
            print("--------------------")
    def filter_vehicles_by_type(self, vehicle_type: VehicleType):
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        filtered_vehicles = {
            vehicle_id: vehicle_info
            for vehicle_id, vehicle_info in self.vehicles.items()
            if vehicle_info["vehicle_type"] == vehicle_type.value
        }
        return filtered_vehicles
# Example Usage
vehicle_records = VehicleRecords()
# Add vehicles using Enum
vehicle_records.add_vehicle(VehicleType.CAR, "Toyota", "Corolla", 2015, "Gasoline", "Automatic", 50000)
vehicle_records.add_vehicle(VehicleType.TRUCK, "Ford", "F-150", 2018, "Diesel", "Manual", 30000)
vehicle_records.add_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR500R", 2020, "Gasoline", "Manual", 10000)
# Display all vehicles
vehicle_records.display_all_vehicles()
# Filter by Enum type
filtered_vehicles = vehicle_records.filter_vehicles_by_type(VehicleType.CAR)
print("Filtered Vehicles by Type:")
for vehicle_id, vehicle_info in filtered_vehicles.items():
    print(vehicle_info)