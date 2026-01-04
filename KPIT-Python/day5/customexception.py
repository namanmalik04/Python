class InvalidDataTypeError(Exception):
    """Custom exception for invalid data types in a list."""

    def __init__(self, invalid_item, expected_type):
        self.invalid_item = invalid_item
        self.expected_type = expected_type
        super().__init__(f"Invalid item '{invalid_item}'. Expected type: {expected_type.__name__}")
 
    # Custom method to suggest correction
    def suggest_fix(self):
        return f"Please replace '{self.invalid_item}' with a {self.expected_type.__name__} value."


# Function to validate list elements
def validate_integer_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    for item in data:
        if not isinstance(item, int):
            # Raise custom exception with details
            raise InvalidDataTypeError(item, int)

    return "Validation successful! All elements are integers."


# Test the function
try:
    numbers = [10, 20, 'thirty', 40]
    print(validate_integer_list(numbers))
except TypeError as te:
        # Handles the case where the input is not a list.
        print(f"TypeError: {te}")
except InvalidDataTypeError as e:
    print(e)  # Default error message
    print(e.suggest_fix())  # Using custom method
except Exception as e:
    # Catch‑all for any other unexpected errors.
    print(f"An unexpected error occurred: {e}")