import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    if strength <= 2:
        result = "Weak"
    elif strength == 3 or strength == 4:
        result = "Medium"
    else:
        result = "Strong"

    return result, feedback

password = input("Enter a password to test: ")
strength, feedback = check_password_strength(password)

print("Password Strength:", strength)
for f in feedback:
    print("-", f)
