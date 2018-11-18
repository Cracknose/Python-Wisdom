"""
	Detta är en demo / ett test med Classer i en class
	detta gör inget annat än att sätta variabler, simpel addition
	och print statements nästat i classer

"""

class myclass:

	def __init__(self):

		self.fname = "Nisse"
		self.lname = "Borat"
		self.cash = 1000
		self.t1 = self.one()
		self.t2 = self.two()


	def payment(self, money):

		self.cash += money
		print(self.fname +" "+self.lname +" Has "+str(self.cash)+" Moneeeeh!")

	class one:

		def printneger(self):
			print("NEEEEGER!!")

	class two:

		def printass(self):
			print("AAAASSSSSS!")


Mythingy = myclass()
Mythingy.payment(200)
Mythingy.t1.printneger()
Mythingy.t2.printass()