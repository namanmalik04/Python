class Vehicle:
    """Represents a vehicle in the fleet."""

    def __init__(self, vehicle_id, vehicle_type, fuel_capacity, maintenance_cost, last_service_days, delivery_rating):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type  # e.g., "Van", "Truck"
        self.fuel_capacity = fuel_capacity  # Liters
        self.maintenance_cost = maintenance_cost  # Last maintenance cost
        self.last_service_days = last_service_days  # Days since last service
        self.delivery_rating = delivery_rating # Rating between 1-5

    def __repr__(self):
        return (f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Fuel: {self.fuel_capacity}, "
                f"Maintenance: {self.maintenance_cost}, Service Days: {self.last_service_days}, Rating: {self.delivery_rating}")


class VehicleFleetManager:
    """Manages a fleet of vehicles."""

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Adds a vehicle to the fleet."""
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to the fleet.")

    def remove_vehicle(self, vehicle_id):
        """Removes a vehicle from the fleet by ID."""
        self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]
        print(f"Vehicle {vehicle_id} removed from the fleet.")

    def get_vehicle(self, vehicle_id):
        """Retrieves a vehicle by its ID."""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def get_vehicles_by_type(self, vehicle_type):
       """Returns a list of vehicles of a specific type."""
       return [vehicle for vehicle in self.vehicles if vehicle.vehicle_type == vehicle_type]

    def calculate_statistic(self, operation):
        """Calculates a statistic (avg, sum, min, max) for maintenance_cost."""
        if not self.vehicles:
            return None  # Handle empty fleet case

        values = [vehicle.maintenance_cost for vehicle in self.vehicles]

        if operation == "avg":
            return sum(values) / len(values)
        elif operation == "sum":
            return sum(values)
        elif operation == "min":
            return min(values)
        elif operation == "max":
            return max(values)
        else:
            return None # Invalid operation

    def filter_greater_than(self, threshold):
        """Filters vehicles where maintenance_cost is greater than the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost > threshold]

    def filter_less_than(self, threshold):
        """Filters vehicles where maintenance_cost is less than the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost < threshold]

    def filter_equal_to(self, threshold):
        """Filters vehicles where maintenance_cost is equal to the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost == threshold]


    def sort_vehicles(self, reverse=False):
        """Sorts vehicles based on maintenance_cost."""
        return sorted(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost, reverse=reverse)

    def find_min_vehicle(self):
        """Finds the vehicle with the minimum maintenance_cost."""
        if not self.vehicles:
            return None
        return min(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

    def find_max_vehicle(self):
        """Finds the vehicle with the maximum maintenance_cost."""
        if not self.vehicles:
            return None
        return max(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

# Example Usage:
fleet_manager = VehicleFleetManager()
v1 = Vehicle("V101", "Van", 60, 500, 30, 4)
v2 = Vehicle("V102", "Van", 70, 600, 15, 5)
v3 = Vehicle("T201", "Truck", 200, 2000, 60, 3)
fleet_manager.add_vehicle(v1)
fleet_manager.add_vehicle(v2)
fleet_manager.add_vehicle(v3)

print(f"Average Maintenance Cost: {fleet_manager.calculate_statistic('avg')}")
print(f"Sum of Maintenance Costs: {fleet_manager.calculate_statistic('sum')}")
print(f"Minimum Maintenance Cost: {fleet_manager.calculate_statistic('min')}")
print(f"Maximum Maintenance Cost: {fleet_manager.calculate_statistic('max')}")

high_maintenance_vehicles = fleet_manager.filter_greater_than(700)
print(f"Vehicles with Maintenance Cost > 700: {high_maintenance_vehicles}")

sorted_by_maintenance = fleet_manager.sort_vehicles()
print(f"Sorted by Maintenance Cost: {sorted_by_maintenance}")

min_maintenance_vehicle = fleet_manager.find_min_vehicle()
print(f"Vehicle with Minimum Maintenance Cost: {min_maintenance_vehicle}")

max_maintenance_vehicle = fleet_manager.find_max_vehicle()
print(f"Vehicle with Maximum Maintenance Cost: {max_maintenance_vehicle}")

 