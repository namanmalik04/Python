from enum import Enum
from typing import Dict, List


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



class BatteryManagementSystem:
    def __init__(self, max_voltage_limit: float, min_voltage_limit: float, max_temp_limit: float):
        self.batteries: Dict[str, Battery] = {}
        self.max_voltage_limit = max_voltage_limit
        self.min_voltage_limit = min_voltage_limit
        self.max_temp_limit = max_temp_limit
        self.alerts: List[str] = []
