from VehicleTypeEnum import VehicleType
from VehicleClass import VehicleRecords

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