import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength Evaluation
    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Moderate ⚠"
    else:
        strength = "Weak ❌"

    return strength, feedback


while True:
    print("\nPassword Complexity Checker")
    print("1. Check Password")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == "2":
        print("Program exited.")
        break

    if choice != "1":
        print("Invalid choice. Try again.")
        continue

    password = input("Enter your password: ")
    strength, feedback = check_password(password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("-", item)
