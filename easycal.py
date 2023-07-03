from datetime import datetime
import json

import discord as discord

client = discord.Client(intents=discord.Intents.default())

def readData():
    global token, channel_read, user_read
    with open("data.txt", "r") as file:
        lines = file.readlines()

    if len(lines) >= 3:
        token = lines[0].strip()
        channel_read = lines[1].strip()
        user_read = lines[2].strip()

        # Verwende die Variablen token, channel und user weiter
        print("Token:", token)
        print("Channel:", channel_read)
        print("User:", user_read)
    else:
        print("Die Datei enthält nicht genügend Zeilen.")

def readDates(embed):
    with open("dates.json", "r") as file:
        json_data = json.load(file)

    for item in json_data["data"]:
        startdate = datetime.strptime(item["startdate"], "%Y-%m-%d").strftime("%d.%m.%Y")
        enddate = datetime.strptime(item["enddate"], "%Y-%m-%d").strftime("%d.%m.%Y")
        user = item["user"]
        status = item["status"]
        number = item["number"]

        if status == "approved":
            status = ":white_check_mark:"
        elif status == "waiting":
            status = ":question:"
        elif status == "declined":
            status = ":x:"

        embed.add_field(name=f"{startdate}" + "-" + f"{enddate}", value=f"{user} #{number} {status}", inline=False)
    return embed
def sendCal():
    embed = discord.Embed(
        title="Abmeldungen",
        description="Abmeldungen per /abmelden {TT.MM.JJJJ} - {TT.MM.JJJJ} {Grund}",
        color=0x657070
    )
    return readDates(embed)

readData()

@client.event
async def on_ready():
    channel = client.get_channel(int(channel_read))
    if channel:
        embed = sendCal()
        await channel.send(embed=embed)
    else:
        user = await client.fetch_user(user_read)
        await user.send("Es wurde kein Kanal gefunden!!")
    await client.close()
client.run(token)