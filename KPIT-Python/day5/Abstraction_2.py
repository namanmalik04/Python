from abc import ABC, abstractmethod

# Abstract Base Class (ABC)
class Tour(ABC):
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    @abstractmethod
    def get_details(self):
        """Abstract method that must be implemented by all subclasses"""
        pass

    @abstractmethod
    def calculate_discounted_price(self, discount):
        """Abstract method to calculate discounted price, must be overridden"""
        pass

# Child class 1: Adventure Tour
class AdventureTour(Tour):
    def __init__(self, destination, price, activity):
        super().__init__(destination, price)
        self.activity = activity

    def get_details(self):
        return f"Adventure Tour: {self.destination} - Activity: {self.activity} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Child class 2: Luxury Tour
class LuxuryTour(Tour):
    def __init__(self, destination, price, hotel):
        super().__init__(destination, price)
        self.hotel = hotel

    def get_details(self):
        return f"Luxury Tour: {self.destination} - Stay at: {self.hotel} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Child class 3: Cultural Tour
class CulturalTour(Tour):
    def __init__(self, destination, price, guide_name):
        super().__init__(destination, price)
        self.guide_name = guide_name

    def get_details(self):
        return f"Cultural Tour: {self.destination} - Guide: {self.guide_name} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Creating tour objects
adventure_tour = AdventureTour("Mount Everest", 3000, "Trekking")
luxury_tour = LuxuryTour("Maldives", 5000, "5-Star Resort")
cultural_tour = CulturalTour("Egypt", 2000, "Dr. Ahmed")

# Displaying tour details and discounted prices
tours = [adventure_tour, luxury_tour, cultural_tour]

for tour in tours:
    print(tour.get_details())
    print(tour.calculate_discounted_price(10))  # Applying a 10% discount
    print()