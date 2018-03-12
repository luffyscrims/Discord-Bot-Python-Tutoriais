#importaçoes Basicas
import discord
from discord.ext import commands
#outras importaçoes
import asyncio
import re
import os
import time
import random

#Variavél para poder usar @client
client = discord.Client()

#montra no terminal se deu certo no loggin do bot,e muda os status do bot no discord
@client.event
async def on_ready():
    print("Bot logado")
    return await client.change_presence(game=discord.Game(name='Status aqui'))


#parte dos comandos
@client.event
async def on_message(message):
    if message.content.lower().startswith('!myinfo'):
        user = message.author
        embed = discord.Embed(color=COR)
        embed.set_thumbnail(url=user.avatar_url)
        await client.send_message(message.channel, embed=embed)
    
    if message.content.lower().startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong" % (userID))

    if message.content.lower().startswith('?img'):
        embed = discord.Embed(color=COR)
        embed.set_image(
            url="https://i.imgur.com/wZvT6CH.jpg")
        await client.send_message(message.channel, embed=embed)

    

client.run('token aki')
