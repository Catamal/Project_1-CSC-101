# This program allows the user to encript and decript a message using ASCII binary code 
# to shift the letters in the message
# 9/11/2026
# Kingsley Wickstrom

# Program_1.py
# ├── Helper functions (conversion & bit operations)
# ├ these will be used in the encryption and decryption functions
# ├── File I/O functions
# ├ these will be used to save and load messages from a file
# ├── Encryption function
# ├ this will take a message and shift the letters using ASCII binary code
# ├── Decryption function
# ├ this will take an encrypted message and shift the letters back to their original positions
# └── Main menu loop

# ---------------------------------------------------------------------------
# Helper functions (conversion & bit operations)
# ---------------------------------------------------------------------------
# Terms I learned while coding this program:
# ord() - returns the integer of a character (ex. ord('A') returns 65)
# chr() - converts an integer to a character (ex. chr(65) returns 'A')
# bin() - converts an integer to a binary string (ex. bin(65) returns '0b1000001')
# zfill() - pads a string with zeros on the left (ex. '1'.zfill(3) returns '001')
# int() - converts a string to an integer (ex. int('1010', 2) returns 10)
# ---------------------------------------------------------------------------

# Start with a binary conversion function to turn text into binary 
# so ASCII can be shifted for encryption/decryption
def text_to_binary(text):
    """Convert text to binary representation of ASCII codes."""
    binary_result = "" # waiting for input
    for character in text: # goes through each character in the text
        ascii_code = ord(character) # gets the ASCII code for the character
        binary_code = bin(ascii_code)[2:].zfill(8) # converts the ASCII code to binary and 
        # pads it with zeros to make it 8 bits long; ASCII is normally 7 bits, but to account
        # for extended ASCII characters I am using 8 bits
        binary_result += binary_code # adds the binary code to the result
    return binary_result # gives input

# Next flip the binary code to shift the letters for encryption/decryption
def flip_binary(binary_str):
    """Flip the binary strings (0s to 1s and 1s to 0s)."""
    flipped = "" # waiting for an input
    for bit in binary_str: # goes through each bit in the binary string
        if bit == '1':
            flipped += '0' # 1 to 0
        else:
            flipped += '1' # 0 to 1
    return flipped # gives input

# Finally convert back to normal text
def binary_to_text(binary_str):
    """ Converts the binary back to human language."""
    text_result = "" # waiting for an input
    for counter in range(0, len(binary_str), 8): # key line where the expression "counter" 
        # will go through len(binary_str) in segments of 8 bits (loops)
        byte = binary_str[counter:counter + 8] # takes the next 8 bits
        ascii_code = int(byte, 2) # converts the 8 bits back to ASCII code
        text_result += chr(ascii_code) # converts the ASCII code back to a character
    return text_result # gives input


# ---------------------------------------------------------------------------
# File I/O functions (Input/Output; save and load messages)
# ---------------------------------------------------------------------------

def init_db():
    open("messages.txt", "a").close() # creates the file if it doesn't exist

def save_to_file(filename, binary_data): # both are placeholders
    """Save encrypted binary data to a text file."""
    with open(filename, "w") as file: # open file for writing
        file.write(binary_data) # write the binary data to the file
    print(f"Encrypted message saved to {filename}") # confirmation message

def read_from_file(filename):
    """Read encrypted binary data from a text file."""
    try: # try to read the file
        with open(filename, "r") as file: # open file for reading
            binary_data = file.read() # read the entire file contents
        return binary_data # return the binary data
    except FileNotFoundError: # if file doesn't exist
        print(f"Error: File '{filename}' not found.") # show error message
        return None # return None if file not found




# ---------------------------------------------------------------------------
# Main menu (I am using the code from the budgeting app as a template for this program)
# ---------------------------------------------------------------------------

MENU = """
==============================
      Encryption App Menu
==============================
1. Encrypt a message
2. Decrypt a message
3. Exit
"""

def main():
    init_db() #init = initialize; db = database
    print("Welcome to the Encryption App!")
    while True:
        print(MENU)
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            encrypt_message() # placeholder expression
        elif choice == "2":
            decrypt_message() # placeholder expression
        elif choice == "3":
            print("Goodbye!") # exit program
            break # continue
        else:
            print("Invalid choice, please pick a number from 1 to 3.") # level 8 error
