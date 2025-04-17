# name: Mark Dymek
# date: 3/23/25
# purpose: Code a program that calculates the average grode of 4 test scores and ask if we want to drop the lowest

studentName = input("What is your name:")  # get users name and setup the constants
itestScore1 = int(input(f"Enter your first test score {studentName}:"))
itestScore2 = int(input(f"Enter your second test score {studentName}:"))
itestScore3 = int(input(f"Enter your third test score {studentName}:"))
itestScore4 = int(input(f"Enter your fourth test score {studentName}:"))
dropLowestGrade = input(f"Do you want to drop the lowest grade {studentName}:")
DECIMAL_PLACES = ".1f"
if (
    itestScore1 < 0 or itestScore2 < 0 or itestScore3 < 0 or itestScore4 < 0
):  # did you enter a negative number?
    print("Test scores cannot be less then 0")
    exit()

if dropLowestGrade != "Y" and dropLowestGrade != "N":
    print("You need to say Y or N")
    exit()

iLowest = itestScore1 # checking which score is the lowest
if itestScore2 < iLowest:
    iLowest = itestScore2
if itestScore3 < iLowest:
    iLowest = itestScore3
if itestScore4 < iLowest:
    iLowest = itestScore4


if dropLowestGrade == "Y":
    faverageScore = (itestScore1 + itestScore2 + itestScore3 + itestScore4 - iLowest) / 3

else:
    faverageScore = (itestScore1 + itestScore2 + itestScore3 + itestScore4) / 4


if faverageScore >= 97:
    sletterGrade = "A+"

elif faverageScore >= 94.0 and faverageScore <= 96.9:
    sletterGrade = "A"

elif faverageScore >= 90.0 and faverageScore <= 93.9:
    sletterGrade = "A-"

elif faverageScore >= 87.0 and faverageScore <= 89.9:
    sletterGrade = "B+"

elif faverageScore >= 84.0 and faverageScore <= 86.9:
    sletterGrade = "B"

elif faverageScore >= 80.0 and faverageScore <= 83.9:
    sletterGrade = "B-"

elif faverageScore >= 77.0 and faverageScore <= 79.9:
    sletterGrade = "C+"

elif faverageScore >= 74.0 and faverageScore <= 76.9:
    sletterGrade = "C"

elif faverageScore >= 70.0 and faverageScore <= 73.9:
    sletterGrade = "C-"

elif faverageScore >= 67.0 and faverageScore <= 69.9:
    sletterGrade = "D+"

elif faverageScore >= 64.0 and faverageScore <= 66.9:
    sletterGrade = "D"

elif faverageScore >= 60.0 and faverageScore <= 63.9:
    sletterGrade = "D-"

else:
    sletterGrade = "F"

if sletterGrade == "A+":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} congratulations!")

if sletterGrade == "A":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} well done!")

if sletterGrade == "A-":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} good job!")

if sletterGrade == "B+":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} keep up the good work!")

if sletterGrade == "B":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} you did well")

if sletterGrade == "B-":
    print(f"{studentName}you have a:{faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} hard work pays off")

if sletterGrade == "C+":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} maybe next time don't party so much")

if sletterGrade == "C":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} is this what you wanted?")

if sletterGrade == "C-":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} hope your studying.")

if sletterGrade == "D+":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} this isn't a good relection of your priorities.")

if sletterGrade == "D":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade}M do your parents know your wasting time?")

if sletterGrade == "D-":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} why are you doing this to yourself?")

if sletterGrade == "F":
    print(f"{studentName} you have a: {faverageScore:{DECIMAL_PLACES}} and your grade is: {sletterGrade} what are you doing with your life?")
