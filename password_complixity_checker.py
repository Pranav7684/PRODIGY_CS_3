import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Strength calculation based on the criteria met
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Strength feedback based on score
    feedback = {
        1: "Very Weak: Try adding more characters.",
        2: "Weak: Consider adding uppercase letters, digits, or special characters.",
        3: "Moderate: You can make it stronger by adding special characters.",
        4: "Strong: Consider adding more length or diversity in characters.",
        5: "Very Strong: Great password!"
    }

    # Output the feedback based on score
    return feedback.get(score, "Very Weak: Password does not meet any criteria.")

# Example usage
password = input("Enter your password: ")
result = password_strength(password)
print(result)
