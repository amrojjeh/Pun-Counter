def GetToken():
	with open("token.txt", "r") as token:
		return token.read()

if __name__ == "__main__":
	with open("token.txt", "r") as token:
		print("Your token is : {}".format(token.read()))