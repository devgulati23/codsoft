import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return None
    
    # Define character pools
    lower = string.ascii_lowercase
    digits = string.digits
    special = '@'  # Use only '@' as the special character
    
    # Ensure the password has exactly one capital letter and at least one of the others
    capital_letter = random.choice(string.ascii_uppercase)
    password = [
        capital_letter,
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters (excluding additional uppercase)
    all_characters = lower + digits + special
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to make it random
    random.shuffle(password)
    
    return ''.join(password)

# User input
try:
    length = int(input("Enter the desired length of your password: "))
    generated_password = generate_password(length)
    if generated_password:
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number.")
