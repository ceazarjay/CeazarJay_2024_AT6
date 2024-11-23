from user_input_validator import UserInputValidator  # This will just import the class from my main Python file

# Two instances of UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Sample inputs
inputs1 = ["10", "-5", "abc", "20"]
inputs2 = ["3", "15", "0", "-10"]

# Validation of the inputs using the validate_positive_integers 
validated1 = validator1.validate_positive_integers(inputs1)
validated2 = validator2.validate_positive_integers(inputs2)

# Print the results
print("Validator 1 results:", validated1)
print("Validator 2 results:", validated2)