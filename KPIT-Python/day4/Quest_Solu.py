from enum import Enum
from typing import Dict, List


# ------------------------------
# Enums
# ------------------------------

class BatteryType(Enum):
    LI_ION = 1
    NIMH = 2
    LEAD_ACID = 3
    SOLID_STATE = 4


class BatteryStatus(Enum):
    CHARGING = 1
    DISCHARGING = 2
    IDLE = 3
    FAULT = 4


# ------------------------------
# Battery Class
# ------------------------------

class Battery:
    def __init__(self, battery_id: str, battery_type: BatteryType,
                 status: BatteryStatus, voltage: float, temperature: float):
        self.battery_id = battery_id
        self.battery_type = battery_type
        self.status = status
        self.voltage = voltage
        self.temperature = temperature

    def __repr__(self):
        return f"<Battery {self.battery_id}: {self.battery_type.name}, {self.voltage}V, {self.temperature}°C>"


# ------------------------------
# Battery Management System
# ------------------------------

class BatteryManagementSystem:
    def __init__(self, max_voltage_limit: float, min_voltage_limit: float, max_temp_limit: float):
        self.batteries: Dict[str, Battery] = {}
        self.max_voltage_limit = max_voltage_limit
        self.min_voltage_limit = min_voltage_limit
        self.max_temp_limit = max_temp_limit
        self.alerts: List[str] = []

    # ---------------------------------------------------------
    # Basic Operations
    # ---------------------------------------------------------

    def add_battery(self, battery: Battery):
        if not isinstance(battery.battery_type, BatteryType):
            raise ValueError("Invalid BatteryType.")
        if not isinstance(battery.status, BatteryStatus):
            raise ValueError("Invalid BatteryStatus.")
        self.batteries[battery.battery_id] = battery

    def remove_battery(self, battery_id: str):
        self.batteries.pop(battery_id, None)

    def update_status(self, battery_id: str, new_status: BatteryStatus):
        if battery_id in self.batteries:
            self.batteries[battery_id].status = new_status

    # ---------------------------------------------------------
    # Monitoring & Calculations
    # ---------------------------------------------------------

    def total_voltage(self):
        return sum(b.voltage for b in self.batteries.values())

    def average_temperature(self):
        return sum(b.temperature for b in self.batteries.values()) / len(self.batteries)

    def battery_with_max_voltage(self):
        return max(self.batteries.values(), key=lambda b: b.voltage)

    def battery_with_min_temperature(self):
        return min(self.batteries.values(), key=lambda b: b.temperature)

    def filter_above_max_temp(self):
        return [b for b in self.batteries.values() if b.temperature > self.max_temp_limit]

    def filter_below_min_voltage(self):
        return [b for b in self.batteries.values() if b.voltage < self.min_voltage_limit]

    # ---------------------------------------------------------
    # Alerts (using lambda)
    # ---------------------------------------------------------

    def generate_alerts(self):
        checker = lambda b: (
            b.temperature > self.max_temp_limit,
            b.voltage > self.max_voltage_limit,
            b.voltage < self.min_voltage_limit
        )

        for b in self.batteries.values():
            over_temp, over_volt, under_volt = checker(b)

            if over_temp:
                self.alerts.append(f"{b.battery_id}: Over Temperature")
            if over_volt:
                self.alerts.append(f"{b.battery_id}: Over Voltage")
            if under_volt:
                self.alerts.append(f"{b.battery_id}: Under Voltage")

    # ---------------------------------------------------------
    # Summaries / Lists / Sorting
    # ---------------------------------------------------------

    def voltage_summary(self):
        return {bid: b.voltage for bid, b in self.batteries.items()}

    def battery_type_list(self):
        return [b.battery_type for b in self.batteries.values()]

    def sort_by_voltage(self):
        return sorted(self.batteries.values(), key=lambda b: b.voltage)

    def sort_by_temperature_desc(self):
        return sorted(self.batteries.values(), key=lambda b: b.temperature, reverse=True)

    def count_by_status(self):
        return {
            status: sum(1 for b in self.batteries.values() if b.status == status)
            for status in BatteryStatus
        }

    # ---------------------------------------------------------
    # Advanced Functions
    # ---------------------------------------------------------

    def predict_charging_completion(self, battery_id: str, charging_rate: float):
        """
        Predict time to reach max voltage limit.
        charging_rate = volts per minute.
        """
        b = self.batteries[battery_id]
        remaining = self.max_voltage_limit - b.voltage
        predictor = lambda diff, rate: diff / rate if rate > 0 else None
        return predictor(remaining, charging_rate)

    def voltage_trend(self, history: List[dict]):
        return [h["voltage"] for h in history]

    def all_batteries_healthy(self):
        return all(
            self.min_voltage_limit <= b.voltage <= self.max_voltage_limit and
            b.temperature <= self.max_temp_limit
            for b in self.batteries.values()
        )
