import random
firstnames = ['John', 'Paul', 'George', 'Ringo']
secondnames = ['Lennon', 'McCartney', 'Harrison', 'Starr']
thirdnames = ['Mick', 'Keith', 'Charlie', 'Ronnie']
fourthnames = ['Jagger', 'Richards', 'Watts', 'Wood']
Mainlist = firstnames + secondnames + thirdnames + fourthnames
print(Mainlist)

# Select 3 random winners
winners = random.sample(Mainlist, 3)

# Print the winners
print(f"The winners are: {', '.join(winners)}")
