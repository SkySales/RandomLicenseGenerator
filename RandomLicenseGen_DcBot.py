import discord
import random
import time
import asyncio

TOKEN = "" #PUT YOUR DISCORD BOT TOKEN HERE

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!key'):
        await message.channel.send("**``!license`` > TO GENRATE YOUR LICESNE KEY!**")

    if message.content.startswith('!license'):
        license = [
            '``39QDH-D7MHH-WDMTD-TM2R9-KM7DB``',
            # YOU CAN ADD MORE RANDOM KEYS HERE
        ]
        await message.channel.send("**License Key: **" + random.choice(license))

@client.event
async def on_ready():
    print("Running Success {0.user}".format(client))

client.run(TOKEN)

#DEVELOPED BY SKY!