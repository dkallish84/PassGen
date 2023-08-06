#/ Based on the 'Tech With Tim' video: https://www.youtube.com/watch?v=XCIBOl3FTKo /#

# Import the required Python packages
import random, string

#/ Create a function to generate the password based on the user requirements /#
def generate_password(length, numbers=True, special_chars=True):
    # Get all of the ASCII letters, numbers, and special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    # Create a string of the letters, add the numbers and special characters
    # when applicable
    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False
    # Run the loop until the generated password meets the length and criteria
    while not meets_criteria or len(pwd) < length:
        # Selecat a random character
        new_char = random.choice(characters)
        # Add it to the password
        pwd += new_char
        # Check if new_char was a number
        if new_char in digits:
            has_number = True
        # Check if new_char was a special character
        elif new_char in special:
            has_special = True
        # Set meets_criteria to True so we can prove it is False and keep the loop going
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
    # Return the generated password
    return pwd

# Prompt the user for their requirements
min_length = int(input('Enter the desired length: '))
needs_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
needs_special = input('Do you want to have special characters (y/n)? ').lower() == 'y'
# Create the password and show the result
pwd = generate_password(min_length, needs_number, needs_special)
# Create a password with a minimum of 10 characters, including numbers and special characters
# pwd = generate_password(10)
print('The generated password is: ', pwd)

#/ End /#