#Author Mark Dymmek
#Date: 2/14/2025
#Purpose: Create python program to calcuate weight on other planets

#Constants
PLANET_MERCURY=0.38
PLANET_VENUS=0.91
PLANET_MOON=0.165
PLANET_MARS=0.38
PLANET_JUPITER=2.34
PLANET_SATURN=0.93
PLANET_URANUS=0.92
PLANET_NEPTUNE=1.12
PLANET_PLUTO=0.066
NUMBER_FORMAT="10,.2f"
MAX_STRING="35s"

#ask your name your weight then display your weight on other planets
sName = input("What is your name?: ")
fWeight = float(input(f"Hello {sName} How much do you weigh?: "))
#calculation
print(f"{sName} here is how much you weigh on the different planets")
print(f"{'Your weight on Mercury:':{MAX_STRING}} {PLANET_MERCURY * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Venus:':{MAX_STRING}} {PLANET_VENUS * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Moon:':{MAX_STRING}} {PLANET_MOON * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Mars:':{MAX_STRING}} {PLANET_MARS * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Jupiter:':{MAX_STRING}} {PLANET_JUPITER * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Saturn:':{MAX_STRING}} {PLANET_SATURN * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Uranus:':{MAX_STRING}} {PLANET_URANUS * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Neptune:':{MAX_STRING}} {PLANET_NEPTUNE * fWeight:{NUMBER_FORMAT}}")
print(f"{'Your weight on Pluto:':{MAX_STRING}} {PLANET_PLUTO * fWeight:{NUMBER_FORMAT}}")

#Prof C. I don't mind if you want to show my code that you tell people who wrote it
