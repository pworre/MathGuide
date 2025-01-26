def LagBruker():
	navn = input("Brukernavn: ")
	passord = input("Passord: ")

def printBruker():
	print(f'Brukernavn: {navn}')

# We have to include this. If not, it will run twice when including in main.py
# It is always "__main__" even if the files is called something else. It basicly means "this file".
if __name__ == "__main__":
	LagBruker()
	printBruker()
