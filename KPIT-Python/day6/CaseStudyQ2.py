'''
Create two classes:
Battery → Represents individual battery cells with 5 attributes (including Enums).
BatteryManagementSystem → Manages a dictionary of Battery objects and performs operations using lambda and comprehensions.
 
-Enums to Use
BatteryType → LI_ION, NIMH, LEAD_ACID, SOLID_STATE
BatteryStatus → CHARGING, DISCHARGING, IDLE, FAULT
 
-Battery Class
Attributes:
battery_id → Unique identifier for the battery.
battery_type → Enum BatteryType.
status → Enum BatteryStatus.
voltage → Current voltage of the battery.
temperature → Current temperature of the battery.
 
BatteryManagementSystem Class
Attributes:
batteries → Dictionary where key = battery_id, value = Battery object.
max_voltage_limit, min_voltage_limit, max_temp_limit → Safety thresholds.
alerts → List of alerts generated.
 
Functionalities (using lambda & comprehensions)
Add a new Battery object to dictionary
     → Validate Enums and store in batteries.
Remove a Battery by ID
Update Battery status:→ Change Enum status dynamically.
Monitoring & Calculation
Calculate total voltage of all batteries.
Calculate average temperature.
Find battery with max voltage
Find battery with min temperature.
Filter batteries above max temperature
Filter batteries below min voltage.
Generate alerts for abnormal conditions:→ Use lambda to check and append alerts.
Create summary dictionary of battery voltages.
Create list of battery types.
Sort batteries by voltage
Sort batteries by temperature descending
Count batteries by status
Predict charging completion time:→ Lambda based on voltage difference and charging rate.
Generate historical voltage trend:→ Extract voltages from logs using [h['voltage'] for h in history].
Check if all batteries are healthy (within limits)

'''

# Solution:
from enum import Enum
 
class BatteryType(Enum):
   LI_ION = "Lithium-Ion"
   NIMH = "Nickel-Metal Hydride"
   LEAD_ACID = "Lead Acid"
   SOLID_STATE = "Solid State"
 
class BatteryStatus(Enum):
   CHARGING = "Charging"
   DISCHARGING = "Discharging"
   IDLE = "Idle"
   FAULT = "Fault"
 
class Battery:
   def __init__(self, battery_id, battery_type: BatteryType, status: BatteryStatus, voltage: float, temperature: float):
       if not isinstance(battery_type, BatteryType):
           raise ValueError("Invalid battery type. Must be BatteryType Enum.")
       if not isinstance(status, BatteryStatus):
           raise ValueError("Invalid battery status. Must be BatteryStatus Enum.")
       
       self.battery_id = battery_id
       self.battery_type = battery_type
       self.status = status
       self.voltage = voltage
       self.temperature = temperature
 
   def __repr__(self):
       return f"Battery(ID={self.battery_id}, Type={self.battery_type.value}, Status={self.status.value}, Voltage={self.voltage}, Temp={self.temperature})"
 
class BatteryManagementSystem:
   def __init__(self, max_voltage_limit=4.2, min_voltage_limit=2.5, max_temp_limit=60):
       self.batteries = {}
       self.max_voltage_limit = max_voltage_limit
       self.min_voltage_limit = min_voltage_limit
       self.max_temp_limit = max_temp_limit
       self.alerts = []
 
   # Add Battery
   def add_battery(self, battery: Battery):
       self.batteries[battery.battery_id] = battery
       print(f"Battery {battery.battery_id} added.")
 
   # Remove Battery
   def remove_battery(self, battery_id):
       if battery_id in self.batteries:
           del self.batteries[battery_id]
           print(f"Battery {battery_id} removed.")
       else:
           print("Battery not found.")
 
   # Update Status
   def update_status(self, battery_id, new_status: BatteryStatus):
       if battery_id in self.batteries:
           self.batteries[battery_id].status = new_status
           print(f"Battery {battery_id} status updated to {new_status.value}.")
       else:
           print("Battery not found.")
 
   # Monitoring & Calculations
   def calculate_total_voltage(self):
       return sum(b.voltage for b in self.batteries.values())
 
   def calculate_average_temperature(self):
       return sum(b.temperature for b in self.batteries.values()) / len(self.batteries) if self.batteries else 0
 
   def battery_with_max_voltage(self):
       return max(self.batteries.values(), key=lambda b: b.voltage)
 
   def battery_with_min_temperature(self):
       return min(self.batteries.values(), key=lambda b: b.temperature)
 
   def filter_above_max_temp(self):
       return {bid: b for bid, b in self.batteries.items() if b.temperature > self.max_temp_limit}
 
   def filter_below_min_voltage(self):
       return {bid: b for bid, b in self.batteries.items() if b.voltage < self.min_voltage_limit}
 
   # Alerts using lambda
   def generate_alerts(self):
       check_alert = lambda b: (
           f"Alert: Battery {b.battery_id} abnormal condition!" 
           if b.voltage > self.max_voltage_limit or b.voltage < self.min_voltage_limit or b.temperature > self.max_temp_limit 
           else None
       )
       self.alerts = [alert for b in self.batteries.values() if (alert := check_alert(b))]
       return self.alerts
 
   # Summary dictionary of voltages
   def summary_voltages(self):
       return {bid: b.voltage for bid, b in self.batteries.items()}
 
   # List of battery types
   def list_battery_types(self):
       return [b.battery_type.value for b in self.batteries.values()]
 
   # Sort batteries by voltage
   def sort_by_voltage(self):
       return sorted(self.batteries.values(), key=lambda b: b.voltage)
 
   # Sort by temperature descending
   def sort_by_temperature_desc(self):
       return sorted(self.batteries.values(), key=lambda b: b.temperature, reverse=True)
 
   # Count batteries by status
   def count_by_status(self):
       return {status.value: sum(1 for b in self.batteries.values() if b.status == status) for status in BatteryStatus}
 
   # Predict charging completion time (simple model)
   def predict_charging_time(self, battery_id, charging_rate=0.1):
       if battery_id in self.batteries and self.batteries[battery_id].status == BatteryStatus.CHARGING:
           remaining = self.max_voltage_limit - self.batteries[battery_id].voltage
           return (lambda r: remaining / r)(charging_rate)
       return None
 
   # Check if all batteries are healthy
   def all_batteries_healthy(self):
       return all(self.min_voltage_limit <= b.voltage <= self.max_voltage_limit and b.temperature <= self.max_temp_limit for b in self.batteries.values())
 
# Example Usage
bms = BatteryManagementSystem()
# Add batteries
b1 = Battery(1, BatteryType.LI_ION, BatteryStatus.CHARGING, 3.7, 35)
b2 = Battery(2, BatteryType.NIMH, BatteryStatus.IDLE, 2.4, 40)
b3 = Battery(3, BatteryType.LEAD_ACID, BatteryStatus.DISCHARGING, 4.3, 65)
 
bms.add_battery(b1)
bms.add_battery(b2)
bms.add_battery(b3)
 
print("\nTotal Voltage:", bms.calculate_total_voltage())
print("Average Temperature:", bms.calculate_average_temperature())
print("Max Voltage Battery:", bms.battery_with_max_voltage())
print("Min Temp Battery:", bms.battery_with_min_temperature())
print("Alerts:", bms.generate_alerts())
print("Summary Voltages:", bms.summary_voltages())
print("Battery Types:", bms.list_battery_types())
print("Sorted by Voltage:", bms.sort_by_voltage())
print("Sorted by Temp Desc:", bms.sort_by_temperature_desc())
print("Count by Status:", bms.count_by_status())
print("Charging Time Prediction for Battery 1:", bms.predict_charging_time(1))
print("All Batteries Healthy?", bms.all_batteries_healthy())