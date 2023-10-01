# Angry Boss
import discord #import discord libarires

client = discord.Client() #discord client

#client event on message
@client.event 
async def on_message(message): # when client types a message

  if message:
         text = "WHAT DO YOU MEAN " +message.content + " !!, YOU'RE FIRED!!" # define text
         await message.channel.send(text) # discord sends data back



client.run() # discord run client
