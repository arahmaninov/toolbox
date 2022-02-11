# simple discord bot
# runs on replit

import os
import discord
import requests
import json

client = discord.Client()

def get_chuck_joke():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  json_data = json.loads(response.text)
  like = json_data["value"]
  return(like)


@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!hello"):
    await message.channel.send("Hello, human!")

  if message.content.startswith("!bot"):
    await message.channel.send("I'm a simple bot")

  if message.content.startswith("!chuck"):
    joke = get_chuck_joke()
    await message.channel.send(joke)

client.run(os.getenv("TOKEN"))