def password_validator(password):
    """
    Validates a password based on the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (e.g., !@#$%^&*()-_=+[]{}|;:'",.<>?/)
    
    Args:
        password (str): The password to validate.
    
    Raises:
        ValueError: If the password does not meet any of the criteria.
    
    Returns:
        bool: True if the password is valid.
    """
    import re

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search(r'\d', password):
        raise ValueError("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*()\-_+=\[\]{}|;:\'",.<>?]', password):
        raise ValueError("Password must contain at least one special character.")

    return True


print(password_validator("Valid1@Password"))  # Should return True
print(password_validator("invalidpassword"))  # Should raise ValueError