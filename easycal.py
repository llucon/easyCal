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

def sendCal():
    embed = discord.Embed(
        title="Abmeldungen",
        description="Abmeldungen per /abmelden {TT.MM.JJJJ} - {TT.MM.JJJJ} {Grund}",
        color=0x657070
    )
    embed.add_field(name="08.07.2023-13.07.2023", value="@lucon. #001 :white_check_mark:", inline=False)
    embed.add_field(name="10.08.2023-13.09.2023", value="@lucon. #002 :question:")

    return embed

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