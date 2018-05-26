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

	def punMade(self, author, pun):
		self.data["total_puns"] += 1
		self.data["puns"].append({"author": author, "pun": pun})
		self.savePuns()

	def badPun(self, index):
		"""Removes a pun via index"""
		self.data["total_puns"] -= 1
		removedPun = self.data["puns"].pop(index)
		self.savePuns()
		return removedPun

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
		pun = self.data["puns"][index]
		return pun

	def getPunsByContent(self, content):
		for pun in self.data["puns"]:
			startingIndex = pun["pun"].find(content)
			if startingIndex == -1:
				continue
			yield pun

	def getTotalPunsByAuthor(self, author):
		return len(list(self.getPunsByAuthor(author)))

def main():
	goodPuns = PunsList("Puns.json")
	goodPuns.punMade("DinglyMate", "Better than your mom")

if __name__ == "__main__":
	main()