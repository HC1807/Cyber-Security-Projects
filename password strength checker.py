import re

# Step 1-5: Functions to check each password criterion
def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return re.search(r'[A-Z]', password) is not None

def check_lowercase(password):
    return re.search(r'[a-z]', password) is not None

def check_number(password):
    return re.search(r'[0-9]', password) is not None

def check_special_char(password):
    return re.search(r'[@$!%*#?&]', password) is not None

# Step 6: Main function to check password strength
def check_password_strength(password):
    if not check_length(password):
        return "Password is too short. Must be at least 8 characters long."
    if not check_uppercase(password):
        return "Password should have at least one uppercase letter."
    if not check_lowercase(password):
        return "Password should have at least one lowercase letter."
    if not check_number(password):
        return "Password should have at least one number."
    if not check_special_char(password):
        return "Password should have at least one special character (@$!%*#?&)."
    
    return "Strong password!"

# Step 7: Input from user
password = input("Enter a password: ")
print(check_password_strength(password))
