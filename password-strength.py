import string

from Assets.weak_password_list import weak_passwords


def strength_checker(password):
    """
    Criteria for password strength:
    1. Password must be at least 12 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one number
    5. Password must contain at least one special character
    6. Not a weak password
    7. Starts or ends with blank space
    """

    if password in weak_passwords:
            return "Password is a weak password"
    if len(password) < 12:
        return "Password is too short (must be at least 12 characters long)"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number"
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character"
    if password[0] == " " or password[-1] == " ":
        return "Password cannot start or end with a blank space"
    return "Password is strong"


print(strength_checker('password'))
