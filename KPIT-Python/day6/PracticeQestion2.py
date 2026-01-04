'''
Abstract Base Class: VehicleComponent (Abstract)
Attributes:  
component_id: str
status: str (e.g., "OK", "Fault")
reading: float (numeric performance metric)
Abstract Methods:
status_message() → Must return a detailed health message.
validate_reading() → Must validate readings and raise exceptions if unsafe.
compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.
 
Derived Classes
Class 1: EngineSensor
Additional Attributes:
rpm: int
temperature: float
max_rpm=6000
Complex Methods:
Override compute_efficiency():
Efficiency = (rpm / max_rpm) * (1 - temperature_penalty)
Use lambda for penalty calculation.
Override status_message():
Include dynamic analysis: "Engine running smoothly" or "Engine alert!" based on condition of status.(if status is not “OK” then "Engine alert!” otherwise "Engine running smoothly")
Override validate_reading():
Raise EngineOverheatException if temperature > 150°C.
Log warnings if rpm exceeds safe range.
 
Class 2: BrakeSensor
Additional Attributes:
pad_thickness: float (in mm)
fluid_level: float (in %)
ideal_thickness=5.0
Complex Methods:
Override compute_efficiency():
Efficiency = (fluid_level / 100) * (pad_thickness / ideal_thickness)
Use lambda for quick ratio calculation.
Override status_message():
Return "Brakes optimal" or "Brake maintenance required" with severity level.
(if status is not “OK” then " Brake maintenance required” otherwise " Brakes optimal ")
 
Override validate_reading():
Raise BrakeFailureException if pad_thickness < 1 mm.
Suggest maintenance schedule dynamically.
 
Custom Exceptions
EngineOverheatException : Raised when engine temperature exceeds safe limit.
BrakeFailureException : Raised when brake pad thickness is critically low.
 
Object Creation
Create 3 EngineSensor objects and 2 BrakeSensor objects.
Store all objects in a list called components.
 
Functions
Implement the following operations:
filter_faulty_components(components)
Return components where status != "OK".
Use list comprehension and isinstance() to group by type.
sort_components_by_efficiency(components)
Sort components by computed efficiency using their compute_efficiency() method.
Use lambda with sorted().
generate_health_report(components)
Output a dictionary:
{
"total_components": int,
"engine_alerts": int,
"brake_alerts": int,
"average_efficiency": float
}
Use dictionary comprehension and map().
 
# EngineSensor Objects
e1 = EngineSensor(component_id="E001", status="OK", reading=85.0, rpm=2500, temperature=95.0)
e2 = EngineSensor(component_id="E002", status="Fault", reading=70.0, rpm=7000, temperature=160.0)
e3 = EngineSensor(component_id="E003", status="OK", reading=90.0, rpm=1500, temperature=110.0)
 
# BrakeSensor Objects
b1 = BrakeSensor(component_id="B001", status="OK", reading=60.0, pad_thickness=4.5, fluid_level=80.0)
b2 = BrakeSensor(component_id="B002", status="Fault", reading=40.0, pad_thickness=0.8, fluid_level=30.0)
 
# Combine into a single list
components = [e1, e2, e3, b1, b2]

'''