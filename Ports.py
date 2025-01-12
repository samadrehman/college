import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special

    def generate_password(self):
        character_pool = ''
        if self.use_uppercase:
            character_pool += string.ascii_uppercase
        if self.use_lowercase:
            character_pool += string.ascii_lowercase
        if self.use_digits:
            character_pool += string.digits
        if self.use_special:
            character_pool += string.punctuation

        if not character_pool:
            raise ValueError("At least one character type must be selected.")

        password = ''.join(random.choice(character_pool) for _ in range(self.length))
        return password

    def generate_multiple_passwords(self, count):
        return {self.generate_password() for _ in range(count)}

def main():
    print("Welcome to the Advanced Password Generator!")
    
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    generator = PasswordGenerator(length, use_uppercase, use_lowercase, use_digits, use_special)

    count = int(input("How many passwords would you like to generate? (default is 1): ") or 1)
    
    print("\nGenerated Passwords:")
    passwords = generator.generate_multiple_passwords(count)
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()