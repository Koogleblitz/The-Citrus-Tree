#workSpace.py
import discord
import random
import json
from discord.ext import commands
import os

# from dotenv import load_dotenv     <- we wouuld put the token into the dotenv file later for securiy reasons


from classList import class_list




#the token connects the code 
TOKEN= 'OTU5ODk5NzYzOTEyODY3ODYw.YkimUQ.zXKtDgtKMjHTK7k_2s4ZYXqdyv0'

# 'client' = our bot
client= discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))   #<- use formate provided by client of this msg


#processes user messages that are on the server, send print statement as a response
@client.event
async def on_message(message):
    username= str(message.author).split('#')[0]   #elemnt [0] is the username sans number
    user_message= str(message.content)
    channel= str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')   #formatted print statement

    #make sure the bot doesnt infinitely respond to itself:
    if message.author== client.user:
        return

    #these user msgs are for messages posted on a specific channel, 'await' tells the channel to send a response msg
    if message.channel.name == 'bot-playground':
        if user_message.lower()== "hello":
            await message.channel.send(f'Hello {username}!')
            await message.channel.send(class_list[4])
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
            return
        elif user_message.lower() == '!random':
            response= f'This is your random number: {random.randrange(1000)}'
            await message.channel.send(response)
            return

    #certain responses can be to user msgs that are posted on any channel as opposed to a specific channel:
    if user_message.lower()== '!anywhere':
        await message.channel.send('This can be used anywhere')
        return

    




client.run(TOKEN)