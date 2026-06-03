def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter")

    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit")

    special_chars = "!@#$%^&*"
    if not any(char in special_chars for char in password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")

    return {"valid": len(errors) == 0, "errors": errors}


validate_password("Abc123!x")  # valid
validate_password("abc")  # too short, no upper, no digit, no special
validate_password("ABCDEFGH")  # no lower, no digit, no special
validate_password("ABCDefgh1!")  # valid
