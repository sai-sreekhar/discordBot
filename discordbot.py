import discord
import os
import requests
import json
import random

client = discord.Client()
sad_words = ["sad","depressed","unhappy","angry","miserable","depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person",
]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data  = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]["a"]
  return quote

def get_joke():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  json_data = json.loads(response.text)
  joke = json_data["value"]
  return joke

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('hello') or msg.startswith('hi'):
    await message.channel.send('Hello!')

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if msg.startswith("$joke"):
    joke = get_joke()
    await message.channel.send(joke)

client.run("OTE4NDY4MzcyMjY4NzQwNjQ5.YbHsVA.Lw_ztTfCUE_44LsKU4TkfIzUJwo")


