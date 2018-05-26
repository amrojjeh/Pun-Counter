import discord
import Token
from PunsList import PunsList

client = discord.Client()
goodPuns = PunsList("Puns.json")
@client.event
async def on_ready():
	print("""
========
user name: {}
user id: {}
user display name: {}
========
""".format(client.user.name, client.user.id, client.user.display_name))


@client.event
async def on_message(message):
	# [pun] PUNMADE! <-- look at previous message by the same author to register pun
	if not message.author.bot and message.content.split()[-1].upper() == "PUNMADE!":
		punAuthor = str(message.author.name.lower())
		pun = ""
		for word in message.content.split():
			if word.upper() == "PUNMADE!":
				pun = pun.strip()
				break
			pun += "{} ".format(word)
		if pun.strip() == "":
			await client.send_message(message.channel, "Da pun need word :((")
			return
		goodPuns.punMade(punAuthor, pun)
		await client.send_message(message.channel, "good pun :)))")

	# Badpun... <-- Remove latest pun
	if not message.author.bot and message.content.lower() == "badpun...":
		if goodPuns.getTotalPuns() > 0:
			await client.send_message(message.channel, "RIP PUN **{}**".format(goodPuns.badPun(goodPuns.getTotalPuns() - 1)['pun']))
		else:
			await client.send_message(message.channel, "All dem puns are bad puns :(")

	# DemPuns <-- Get a list of all dem puns
	if not message.author.bot and message.content.lower() == "dempuns":
		puns = goodPuns.getPuns()
		description = ""
		for pun in puns:
			description += "{}: {}\n".format(pun['author'], pun['pun'])
		em = discord.Embed(title="Here dem puns :)", description=description, color=0xFF0000)
		await client.send_message(message.channel, embed=em)

	# WhoPun [author] <-- Get a list of puns made by the author
	if not message.author.bot and message.content.lower().startswith("whopun "):
		author = message.content.replace("whopun ", "").lower()
		puns = goodPuns.getPunsByAuthor(author)
		description = ""
		for pun in puns:
			description += "{}\n".format(pun)
		em = discord.Embed(title="'er dem puns by {}".format(author), description=description, color=0xFF0000)
		await client.send_message(message.channel, embed=em)

if __name__ == "__main__":
	client.run(Token.GetToken())