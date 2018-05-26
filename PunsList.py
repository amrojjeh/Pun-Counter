import os.path
import json

class PunsList:
	def __init__(self, punsLocation):
		"""Loads data, if non exist then it shall create data"""
		if os.path.isfile(punsLocation):
			self.loadPuns()
		else:
			self.savePuns()

	def punMade(self, pun):
		pass
	def badPun(self, pun):
		pass
	def loadPuns(self):
		pass
	def savePuns(self):
		pass

def main():
	goodPuns = PunsList("Puns.json")

if __name__ == "__main__":
	main()