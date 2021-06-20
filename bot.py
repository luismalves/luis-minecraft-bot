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
    
    if message.content.startswith('>hello') or message.content.startswith('>hello'):
        await message.channel.send('Heyo! Para começar o servidor usem $start_minecraft')

    if message.content.startswith('$start_minecraft'):
        payload = json.dumps({
        "command": "start"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        await message.channel.send('Server is starting! Wait 30s...')

    if message.content.startswith('$stop_minecraft') and message.content.endswith(os.getenv('STOP_KEYWORD')):
        payload = json.dumps({
        "command": "stop"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        await message.channel.send('Server is stopping...')

client.run(os.getenv("DISCORD_TOKEN"))