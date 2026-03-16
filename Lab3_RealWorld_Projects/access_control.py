# access_control.py

# Function to compute access level
def compute_access_level(control, favorite_artist):
    return control * 3 + len(favorite_artist)

# Function to validate access against threshold
def validate_access(level, control):
    threshold = control * 5
    return level >= threshold

# Decorator to log authorization steps
def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper