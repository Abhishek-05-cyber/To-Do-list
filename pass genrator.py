import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")