# --------------------------------------------------------------
#   Sensor hierarchy demo with utility functions
# --------------------------------------------------------------
from typing import List, Dict
 
# Custom Exceptions
class SensorError(Exception):
    """Base class for all sensor‑related errors."""
 
 
class InvalidReadingError(SensorError):
    """Raised when an attempt is made to set a reading that is not numeric."""
    def __init__(self, reading, message: str = "Invalid sensor reading"):
        super().__init__(f"{message}: {reading}")
        self.reading = reading
 
 
class AlertError(SensorError):
    """Raised when an alert operation fails (e.g., duplicate alerts)."""
    pass

# ----------------------------------------------------------------------
# Base Class: Sensor
# ----------------------------------------------------------------------
class Sensor:
    """
    Basic sensor representation.

    Attributes
    ----------
    sensor_id : str
        Unique identifier of the sensor.
    location : str
        Physical location of the sensor.
    reading : float
        Current measurement value.
    unit : str
        Unit of the reading (e.g., "°C", "%").
    alerts : list
        List of active alerts.
    metadata : dict
        Arbitrary meta‑information (manufacturer, model, etc.).
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list = None,
        metadata: dict = None,
    ) -> None:
        self.sensor_id: str = sensor_id
        self.location: str = location
        self.reading: float = reading
        self.unit: str = unit
        self.alerts: list = alerts or []
        self.metadata: dict = metadata or {}

    def __repr__(self) -> str:
        """Return an informative string representation."""
        # return (
        #     f"{self.__class__.__name__}"
        #     f"(ID={self.sensor_id}, Location={self.location}, "
        #     f"Reading={self.reading}{self.unit})"
        # )
        return f"{self.__dict__}"

    def status_message(self) -> str:
        """Default status subclasses override this."""
        return "Sensor operational"

    # ------------------------------------------------------------------
    # Getters / Setters
    # ------------------------------------------------------------------
    def get_reading(self) -> float:
        """Return the current reading."""
        return self.reading

    def set_reading(self, value: float) -> None:
        """
        Update the reading.

        Raises
        ------
        InvalidReadingError
            If ``value`` is not a numeric type.
        """
        if not isinstance(value, (int, float)):
            raise InvalidReadingError(value, "Reading must be numeric")
        self.reading = float(value)


# ----------------------------------------------------------------------
# Derived Class: TemperatureSensor
# ----------------------------------------------------------------------
class TemperatureSensor(Sensor):
    """
    Temperature‑specific sensor.

    Additional Attributes
    ---------------------
    historical_readings : list
        Past temperature values used for analytics.
    calibration_values : dict
        Calibration parameters (e.g., offset, scale).
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list,
        metadata: dict,
        historical_readings: list = None,
        calibration_values: dict = None,
    ) -> None:
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.historical_readings: list = historical_readings or []
        self.calibration_values: dict = calibration_values or {"offset": 0.0, "scale": 1.0}

    # ------------------------------------------------------------------
    # Overridden behaviour
    # ------------------------------------------------------------------
    def status_message(self) -> str:
        """Temperature‑specific status based on a comfortable range."""
        if 15 <= self.reading <= 35:
            return "Temperature Sensor: Normal"
        return "Temperature Sensor: Alert"

    # ------------------------------------------------------------------
    # Temperature‑specific utilities
    # ------------------------------------------------------------------
    def average_temperature(self) -> float:
        """Return the average of ``historical_readings`` (0 if empty)."""
        if not self.historical_readings:
            return 0.0
        return sum(self.historical_readings) / len(self.historical_readings)

    def apply_calibration(self) -> None:
        """
        Adjust ``self.reading`` in‑place using calibration data.

        The formula: (reading + offset) * scale
        """
        offset = self.calibration_values.get("offset", 0.0)
        scale = self.calibration_values.get("scale", 1.0)
        self.reading = (self.reading + offset) * scale


# ----------------------------------------------------------------------
# Derived Class: HumiditySensor
# ----------------------------------------------------------------------
class HumiditySensor(Sensor):
    """
    Humidity‑specific sensor.

    Additional Attributes
    ---------------------
    sensor_age_years : int
        Age of the sensor in years.
    maintenance_log : list
        Record of maintenance activities.
    performance_metrics : dict
        Metrics such as accuracy and response time.
    """

    def __init__(
        self,
        sensor_id: str,
        location: str,
        reading: float,
        unit: str,
        alerts: list,
        metadata: dict,
        sensor_age_years: int,
        maintenance_log: list = None,
        performance_metrics: dict = None,
    ) -> None:
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.sensor_age_years: int = sensor_age_years
        self.maintenance_log: list = maintenance_log or []
        self.performance_metrics: dict = performance_metrics or {}

    # ------------------------------------------------------------------
    # Overridden behaviour
    # ------------------------------------------------------------------
    def status_message(self) -> str:
        """Humidity‑specific status based on an optimal range."""
        if 30 <= self.reading <= 60:
            return "Humidity Sensor: Optimal"
        return "Humidity Sensor: Alert"

    # ------------------------------------------------------------------
    # Humidity‑specific utilities
    # ------------------------------------------------------------------
    def predict_remaining_life(self) -> int:
        """
        Simple predictive model: assume a 10‑year design life.

        Returns
        -------
        int
            Remaining years (floor at 0).
        """
        return max(0, 10 - self.sensor_age_years)

    def last_maintenance(self):
        """Return the most recent maintenance entry, or ``None`` if log is empty."""
        return self.maintenance_log[-1] if self.maintenance_log else None

 # ----------------------------------------------------------------------
# Helper Functions operating on a list of Sensor objects
# ----------------------------------------------------------------------
def filter_sensors_with_alerts(sensors: List[Sensor]) -> List[Sensor]:
    """
    Return only sensors that have at least one active alert.

    Parameters
    ----------
    sensors : list of Sensor

    Returns
    -------
    list of Sensor
    """
    return [sensor for sensor in sensors if sensor.alerts]