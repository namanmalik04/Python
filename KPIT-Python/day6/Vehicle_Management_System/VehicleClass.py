from VehicleTypeEnum import VehicleType 


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