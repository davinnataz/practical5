COLOUR_TO_CODE = {"Absolute Zero":"#0048ba", "Acid Green":"#b0bf1a", "AliceBlue":"f0f8ff",
                  "Amethyst":"#9966cc", "Aqua":"#00ffff", "Banana Yellow":"#ffe135", "Bistre":"#3d2b1f",
                  "Black":"#000000", "Blue Bell":"#a2a2d0", "Bright Lilac":"#d891ef"}

for colour,code in COLOUR_TO_CODE.items():
    print(f"This {colour} code is {code}")

colour_choose = input("Enter your colour :")
while colour_choose !="":
    print(f"This {colour_choose} code is {code}")
    colour_choose = input("Enter your colour :")