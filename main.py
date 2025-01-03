# Project - Text to Morse code converter
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": " "}

# text input
text_input = input("Type the message you need to convert to morse code -").upper()
# Conditions so that only valid input is accepted
morse_list = [] # Combine all letter in one list
for char in text_input:
    if char in MORSE_CODE_DICT.keys(): # Check if we have valid code for letter
        if char == " ":
            morse_list.append(" ")
        else:
            morse_list.append(MORSE_CODE_DICT[char])
    else:
        print("ERROR - Enter only Alpha-Numeric input."
              "Allowed symbols - [, . ( ) ? - and space]")
        break
else:
    for code in morse_list:
        print(code, end=" ")