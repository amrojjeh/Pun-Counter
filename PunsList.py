import os.path
import json

class PunsList:
	def __init__(self, punsLocation):
		"""Loads data, if non exist then it shall create data"""
		self.data = {
			"total_puns" : 0,
			"puns" : []
		}
		self.punsLocation = punsLocation
		if os.path.isfile(punsLocation):
			self.loadPuns()
		else:
			self.savePuns()

	def punMade(self, pun):
		pass
	def badPun(self, pun):
		pass

	def loadPuns(self):
		with open(self.punsLocation, "r") as punsFile:
			self.data = json.load(punsFile)

	def savePuns(self):
		with open(self.punsLocation, "w") as punsFile:
			json.dump(self.data, punsFile, indent=4)

	def getData(self):
		return self.data

	def getTotalPuns(self):
		return self.data["total_puns"]

	def getPunsByAuthor(self, author):
		for pun in self.data["puns"]:
			if not author in pun.values():
				continue
			else:
				yield pun["pun"]

	def getPunByIndex(self, index):
		pass

	def getPunsByContent(self, search):
		pass

	def getTotalPunsByAuthor(self, author):
		return len(list(self.getPunsByAuthor(author)))

def main():
	goodPuns = PunsList("Puns.json")
	print("Total puns : {}".format(goodPuns.getTotalPuns()))
	print("Puns by Dinglydo : {}".format(list(goodPuns.getPunsByAuthor("Dinglydo"))))
	print("Total puns by Dinglydo : {}".format(goodPuns.getTotalPunsByAuthor("Dinglydo")))

if __name__ == "__main__":
	main()