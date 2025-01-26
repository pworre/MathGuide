def LagBruker():
	navn = input("Brukernavn: ")
	passord = input("Passord: ")

def printBruker():
	print(f'Brukernavn: {navn}')

# We have to include this. If not, it will run twice when including in main.py
if __name__ == "__addons__":
	LagBruker()
	printBruker()
