import discord
import random
import asyncio
import aiohttp
import json
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = os.environ["TOKEN"]

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name="with humans"))

@client.command(name='hello',description='Just says Hello.',brief='Just says Hello.',aliases=['Hello','Hello!'])
async def hello():
    await client.say("Hello!")

@client.command(name='add',description='Adds two numbers together.',brief='Adds two numbers together.',aliases=['Add','addition','Addition'])
async def add(number,number2):
        answer = float(number) + float(number2)
        await client.say(answer)

@client.command(name='square',description='Squares the entered number.',brief='Squares the entered number.',aliases=['Square'])
async def square(number):
    squared_value = float(number) * float(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command(name='roll',description='Rolls the dice to get an answer from 1 to 6.',brief='Rolls the dice to get an answer from 1 to 6.',aliases=['Roll','Dice','dice'])
async def roll():
    result = random.randint(1, 6)
    await client.say(result)

@client.command(name='coinflip',description='Flips a coin.',brief='Flips a coin.',aliases=['coin','Coin','flip','Flip','Coinflip'])
async def coinflip():
    list = ["Heads","Tails"]
    await client.say(random.choice(list))

@client.command(name='8ball',description='Answers from the beyond.',brief="Answers from the beyond.",aliases=['eight_ball', 'eightball', '8-ball'])
async def eight_ball():
    possible_responses = ['That is a resounding no','It is not looking likely','Too hard to tell','It is quite possible','Definitely',]
    await client.say(random.choice(possible_responses))

@client.command(name='bitcoin',description='Shows the current price of Bitcoin in USD.',brief='Shows the current price of Bitcoin in USD.',aliases=['Bitcoin'])
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command(name='hidden command',description='...',brief='...')
async def bitch():
    await client.say('Jacob gay')

client.run(TOKEN)

