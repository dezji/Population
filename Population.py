# Author Name: Deziallia Morris

# Set up variables and get user input to store in variables
startingOrganisms = int(input("Starting organisms: "))
organisms = startingOrganisms
averageDailyIncrease = float(input("Average daily increase (percent): ")) / 100
numberOfDays = int(input("Number of days to multiply: "))

# Print columns
print("Days Approximate\tPopulation")

# Loop for each day, and tab for columns to line up. Format organisms to float
for day in range(1, numberOfDays + 1):
    print(day, '\t\t\t\t\t', float(organisms))
    organisms = (organisms * averageDailyIncrease) + organisms
