import re

# Email entered by user
userEmail = input("Enter your email: ")

# Validation function
def validation(email):
    valid = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2,})+$"
    
    # Validate if the re and the email parameter have the same format
    if re.match(valid, email, re.IGNORECASE):
        return f"The email {email} is valid"
    return f"The email {email} isn't valid"

validationResult = validation(userEmail)
print(validationResult)