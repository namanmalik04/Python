class Car:
    company_name = "AutoMobiles Ltd"   # Class variable
    car_count = 0                      # Class variable

    def __init__(self, model, year):
        self.model = model             # Instance variable
        self.year = year               # Instance variable
        Car.car_count += 1             

    def show_details(self):
        print(f"Model: {self.model}, Year: {self.year}, Company: {Car.company_name}")

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    @classmethod
    def get_car_count(cls):
        return cls.car_count


# Creating objects
c1 = Car("Sedan X", 2022)
c2 = Car("SUV Pro", 2023)

c1.show_details()
c2.show_details()

# Changing class variable using classmethod
Car.change_company("Global Auto Corp")

c1.show_details()
c2.show_details()

print("Total Cars Manufactured:", Car.get_car_count())
