import os
import discord
import requests
import json

intents = discord.Intents.default()
client = discord.Client(intents=intents)

url = os.getenv('WEBHOOCK')
headers = { 'Content-Type': 'application/json' }

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$start'):
        payload = json.dumps({
        "command": "start"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        await message.channel.send('Server is starting! Wait 30s...')

    if message.content.startswith('$stop') and message.content.endswith('luis'):
        payload = json.dumps({
        "command": "stop"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        await message.channel.send('Server is stopping...')

client.run(os.getenv('DISCORD_TOKEN'))