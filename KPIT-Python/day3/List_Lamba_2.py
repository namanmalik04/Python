import datetime

# Sample Vehicle Inventory (List of Dictionaries)
vehicles = [
    {"make": "Toyota", "model": "Camry", "year": 2022, "color": "Silver", "vin": "12345ABC", "price": 25000, "mileage": 15000, "category": "Sedan"},
    {"make": "Honda", "model": "Civic", "year": 2023, "color": "Blue", "vin": "67890DEF", "price": 23000, "mileage": 8000, "category": "Sedan"},
    {"make": "Ford", "model": "F-150", "year": 2021, "color": "Black", "vin": "13579GHI", "price": 35000, "mileage": 22000, "category": "Truck"},
    {"make": "Chevrolet", "model": "Equinox", "year": 2022, "color": "White", "vin": "24680JKL", "price": 27000, "mileage": 12000, "category": "SUV"},
    {"make": "Tesla", "model": "Model 3", "year": 2023, "color": "Red", "vin": "11223MNO", "price": 45000, "mileage": 5000, "category": "Electric"},
    {"make": "Toyota", "model": "Corolla", "year": 2020, "color": "Gray", "vin": "44556PQR", "price": 20000, "mileage": 30000, "category": "Sedan"},
    {"make": "Honda", "model": "CR-V", "year": 2023, "color": "Silver", "vin": "77889STU", "price": 30000, "mileage": 10000, "category": "SUV"},
    {"make": "Ford", "model": "Mustang", "year": 2021, "color": "Yellow", "vin": "99001VWX", "price": 40000, "mileage": 18000, "category": "Sports Car"},
    {"make": "Chevrolet", "model": "Tahoe", "year": 2022, "color": "Black", "vin": "22334YZ", "price": 50000, "mileage": 15000, "category": "SUV"},
    {"make": "Tesla", "model": "Model Y", "year": 2023, "color": "White", "vin": "55667ABC", "price": 55000, "mileage": 7000, "category": "Electric"}
]

# 1. Get all vehicles
def get_all_vehicles():
    return vehicles

# 2. Filter vehicles by make (using comprehension)
def filter_by_make(make):
    return [v for v in vehicles if v["make"] == make]

# 3. Filter vehicles by year (using comprehension)
def filter_by_year(year):
    return [v for v in vehicles if v["year"] == year]

# 4. Filter vehicles by price range (using comprehension)
def filter_by_price_range(min_price, max_price):
    return [v for v in vehicles if min_price <= v["price"] <= max_price]

# 5. Get vehicle details by VIN
def get_vehicle_by_vin(vin):
    return next((v for v in vehicles if v["vin"] == vin), None) #Returns None if not found

# 6. Calculate the average price of all vehicles
def average_price():
    return sum(v["price"] for v in vehicles) / len(vehicles)

# 7. Find the most expensive vehicle (using lambda and max)
def most_expensive_vehicle():
    return max(vehicles, key=lambda v: v["price"])

# 8. Find the cheapest vehicle (using lambda and min)
def cheapest_vehicle():
    return min(vehicles, key=lambda v: v["price"])

# 9. Sort vehicles by price (ascending) (using sorted and lambda)
def sort_by_price_asc():
    return sorted(vehicles, key=lambda v: v["price"])

# 10. Sort vehicles by mileage (descending) (using sorted and lambda)
def sort_by_mileage_desc():
    return sorted(vehicles, key=lambda v: v["mileage"], reverse=True)

# 11. Filter vehicles by category (using comprehension)
def filter_by_category(category):
    #return [v for v in vehicles if v["category"] == category]
    return list(filter(lambda x: x["category"]==category, vehicles))

print('***** filter o/p ****************-----------------------')
print(filter_by_category('Sedan'))
print('--------------------------------------------')

# 12. Get a list of all makes (using comprehension)
def get_all_makes():
    return list(set(v["make"] for v in vehicles))  #Use set to avoid duplicates

# 13.  Update vehicle price by VIN
def update_price_by_vin(vin, new_price):
    for v in vehicles:
        if v["vin"] == vin:
            v["price"] = new_price
            return True
    return False

# 14. Add a new vehicle to the inventory
def add_vehicle(vehicle_data):
    vehicles.append(vehicle_data)

'''
Why next is used here
One-shot search - We only need the first matching vehicle, not a list of all matches. 
next stops iterating as soon as it finds a match, making it more efficient than building an intermediate list.

Default handling - By providing None as the default, the code avoids a StopIteration exception when no vehicle matches the VIN. Instead, None is passed to remove.
What happens when the VIN is not found
next(..., None) returns None.
vehicles.remove(None) tries to delete None from the list.
Because None is not an element of vehicles, Python raises ValueError: list.remove(x): x not in list.

'''
# 15. Remove a vehicle by VIN
def remove_vehicle_by_vin(vin):
    return vehicles.remove(next((v for v in vehicles if v["vin"] == vin), None))

try:
    print('remove_vehicle_by_vin----------------->')
    print(remove_vehicle_by_vin("12345ABC"))
except ValueError:
    print('invalid vin ')

# 16. Count the number of vehicles of a specific make (using comprehension)
def count_vehicles_by_make(make):
    return sum(1 for v in vehicles if v["make"] == make)

# 17. Get vehicles with mileage less than a certain value (using comprehension)
def filter_by_mileage(max_mileage):
    return [v for v in vehicles if v["mileage"] < max_mileage]

# 18. Create a list of VINs for all vehicles (using comprehension)
def get_all_vins():
    return [v["vin"] for v in vehicles]

# 19. Calculate total inventory value (using comprehension)
def total_inventory_value():
    return sum(v["price"] for v in vehicles)

# 20. Filter vehicles manufactured after a certain year (using comprehension)
def filter_by_year_after(year):
    return [v for v in vehicles if v["year"] > year]

# 21.  Check if a vehicle with a given VIN exists (using lambda and any)
def vehicle_exists(vin):
    return any(v["vin"] == vin for v in vehicles)

# 22.  Get the average mileage of vehicles within a specific category
def average_mileage_by_category(category):
    category_vehicles = [v for v in vehicles if v["category"] == category]
    if category_vehicles:
        return sum(v["mileage"] for v in category_vehicles) / len(category_vehicles)
    return 0

# 23.  Find the newest vehicle (using lambda and max)
def newest_vehicle():
    return max(vehicles, key=lambda v: v["year"])

# 24.  Get a list of vehicle colors (using comprehension)
def get_all_colors():
    return list(set(v["color"] for v in vehicles))

# 25. Apply a discount to all vehicles of a specific make (using lambda and map)
def apply_discount_to_make(make, discount_percentage):
    return list(map(lambda v: {**v, "price": v["price"] * (1 - discount_percentage/100)} if v["make"] == make else v, vehicles))

# 26.  Get vehicles with a specific color and make (using comprehension)
def filter_by_color_and_make(color, make):
    return [v for v in vehicles if v["color"] == color and v["make"] == make]

# 27.  Convert vehicle data to a specific format (e.g., CSV-like string) using a lambda function
def format_vehicle_data(vehicle):
    return f"{vehicle['make']},{vehicle['model']},{vehicle['year']},{vehicle['price']}"

# 28. Get vehicles with mileage between a range and category
def filter_by_mileage_and_category(min_mileage, max_mileage, category):
    return [v for v in vehicles if min_mileage <= v["mileage"] <= max_mileage and v["category"] == category]

# 29. Check if any vehicles are older than a certain age
def has_old_vehicles(age):
    current_year = datetime.datetime.now().year
    return any(current_year - v["year"] > age for v in vehicles)

# 30. Get vehicles sorted by year and then by price
def sort_by_year_and_price():
    return sorted(vehicles, key=lambda v: (v["year"], v["price"]))



# Example Usage
print("All Vehicles:", get_all_vehicles())
print("\nToyota Vehicles:", filter_by_make("Toyota"))
print("\nVehicles between $25,000 and $40,000:", filter_by_price_range(25000, 40000))
print("\nMost Expensive Vehicle:", most_expensive_vehicle())
print("\nSorted by Price (Ascending):", sort_by_price_asc())