def main() -> None:
    """Main function."""
    inventory = []
    add_vehicle(inventory, "ABC123", "Car", "Toyota", 2020, "Red", "Gasoline")
    add_vehicle(inventory, "DEF456", "Truck", "Ford", 2015, "Blue", "Diesel")
    display_vehicle_info(inventory, "ABC123")
    record_sales(inventory, "ABC123", "2022-01-01", 20000, "John Doe")
    display_sales_history(inventory, "ABC123")
    record_maintenance(inventory, "DEF456", "2022-02-01", "Oil change", 100)
    display_maintenance_history(inventory, "DEF456")
    

if __name__ == "__main__":
    main()
 

'''This is the  ExampleforExplicitMainFun '''