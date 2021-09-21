import os
import discord
import requests
import json
import random
import emoji
from discord import Embed, File
from keep_alive import keep_alive

client = discord.Client()

colors = [0xFFC0CB, 0xFFB6C1, 0xFF69B4, 0xFF1493,	0xE6E6FA, 0xD8BFD8, 0xDDA0DD, 0xDA70D6, 0xEE82EE, 0xFF00FF,0xFF00FF]

specific_words = ["word1","word2"]

starter_encouragements = ["Cheer up!","Hang in there.","You are a great person / bot"]

messages = ["msg1","msg2","msg3","msg4","msg5","msg6","msg7","msg8","msg9","msg10","msg11","msg12", "msg13"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " ~" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("person"):
    
    arg = msg.split("personname ",1)[1].lower()
    
    if arg == "show":
      #await message.channel.send('Hello!')

     # embed = Embed(title = "Now online!", description = "Bihir is online", colour = random.choice(colors))
     # fields = [("Name", "Value", True), ("Another field", "Other val", True)]
      #embed.add_field(name = "Name", value = "Value", inline = False)
      #for name, value, inline in fields:
      #  embed.add_field(name = name, value = value, inline = inline)
 
      #await message.channel.send(embed = embed)

      await message.channel.send(file = File("pic" + str(random.randint(1,17)) + ".jpg"))  

    if arg == "prompt1":
      await message.channel.send(random.choice(messages))

    if arg == "prompt2":
      embed = Embed(title = "reply1", description = "reply2", colour = random.choice(colors))
      file = discord.File("vid1.mp4")
      embed.set_thumbnail(url = "attachment://vid1.mp4")
      await message.channel.send(embed = embed)
      await message.channel.send(file = file)


  if msg.startswith("game prompt"):
    embed = Embed(title = "game name", description = "phrase1 " + str(random.randint(100,110)) + "phrase2", colour = 0x000000)
    await message.channel.send(embed = embed) 

  if any(word in msg for word in specific_words):
    embed = Embed(title = "reply1embed", description = "reply2embed", colour = random.choice(colors))
    file = discord.File("pic1.jpg")
    embed.set_image(url = "attachment://pic1.jpg")
    await message.channel.send(embed = embed, file = file)

keep_alive()
client.run(os.environ['TOKEN'])      

