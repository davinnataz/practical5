"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
def main():
    print_formatted_states(CODE_TO_NAME)
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()
    print()
    print_formatted_states(CODE_TO_NAME)

def print_formatted_states(code_to_name):
    for code in code_to_name:
        print(code, "is", CODE_TO_NAME[code])

main()