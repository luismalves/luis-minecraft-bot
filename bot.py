import os
import discord
import requests
import json

intents = discord.Intents.default()
client = discord.Client(intents=intents)

url = os.getenv("WEBHOOCK")
headers = { 'Content-Type': 'application/json' }

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.content.startswith('$'):
        payload = json.dumps({
        "command": message.content
        })
        response = requests.request("POST", url, headers=headers, data=payload)

client.run(os.getenv("DISCORD_TOKEN"))