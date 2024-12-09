def taxiCalculator(people, maxpeople):
    nbrTaxis = (people + maxpeople -1) // maxpeople
    return nbrTaxis

people = int(input('enter the total number of people'))
capacity = int(input('enter the max number of people per taxi'))
totalTaxis = taxiCalculator(people,capacity)
print(f"number of taxis needed : {totalTaxis}")