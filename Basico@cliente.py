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
    if message.content.lower().startswith('!info'):
        botmsg = await client.send_message(message)
    if message.content.lower().startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong" % (userID))

    if message.content.lower().startswith('/diz') and message.author.id != 'IDDOBOT':
        import re
        mensagem = re.sub('/diz ', '', message.content)
        canaltxt = mensagem.split(' ', 1)
        canaltxt = str(canaltxt[0])
        mensagem = re.sub(canaltxt, '', mensagem)
        canal = discord.utils.find(lambda r: r.name == canaltxt or r.id == canaltxt or r.mention == canaltxt,
                                   message.author.server.channels)
        await client.send_message(canal, '' + mensagem)
        await client.delete_message(message)

    if message.content.lower().startswith('?img'):
        embed = discord.Embed(color=COR)
        embed.set_image(
            url="https://i.imgur.com/wZvT6CH.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('r!mutar'):
        cargomod = discord.utils.find(lambda r: r.name == "Adminstrador", message.server.roles)
        if message.author.top_role.position >= cargomod.position:
            member = re.sub('r!mutar ', '', message.content)
            member = discord.utils.find(lambda r: r.mention == member, message.server.members)
            cargomute = discord.utils.find(lambda r: r.name == "Mutados", message.server.roles)
            await client.add_roles(member, cargomute)
            await client.send_message(message.channel,
                                      '{0.mention} foi mutado por : {1.mention}'.format(member, message.author))
        else:
            await client.send_message(message.channel, '**Você não tem permissão para usar esse comando!**  :rage:')

client.run('token aki')
