# Mark Dymek
# 3/9/25
# Purpose: Code a temp converter from F to C and C to F

# Contants:
fFREEZINGC = 0.0
fFREEZINGF = 32.0
fBOILINGC = 100.0
fBOILINGF = 212.0
fCONVERTC = 9.0 / 5.0
fCONVERTF = 5.0 / 9.0
NUMBER_CONVERT = ".1F"

# welcome message
print("Hello, welcome to Mark's temperature converter!")
# inputs
fTemp = float(input("Please enter a temp: "))
sScale = input("Enter F or f for Fahrenheit or C or c for Celsius: ")

# did you enter a proper character?
if not (sScale == "F" or sScale == "f" or sScale == "C" or sScale == "c"):
    print("You did not enter a F or C")
    raise SystemExit
if sScale == "F" or sScale == "f":
    if fTemp > fBOILINGF:
        print("Temp cannot be greater than 212")
    elif fTemp < fFREEZINGF:
        print("Temp cannot be less than 32")
    else:
        fCel = (fTemp - fFREEZINGF) * fCONVERTF
        print(f"The celsius equivalent is : {fCel:{NUMBER_CONVERT}}")
elif sScale == "C" or sScale == "c":
    if fTemp < fFREEZINGC:
        print("Temp cannot be less than 0")
    elif fTemp > fBOILINGC:
        print("Temp cannot be great than 100")
    else:
        fFahr = (fTemp * fCONVERTC) + fFREEZINGF
        print(f"The Fahrenheit equivalent is : {fFahr:{NUMBER_CONVERT}}")
