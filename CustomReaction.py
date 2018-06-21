import discord


COR = 0x690FC3
msg_id = None
msg_user = None
client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE !')
    print(client.user.name)
    print(client.user.id)
    print('------Vagner Tutorial----')
    print('------LabNegro-------')
    print('-----Tutorial Cargo Custom Emoji-----')

"""
link do emojis dos elos do league of legends para download .
https://drive.google.com/drive/folders/1dFHnj0RWG23iR2JfoEr56RdUs9flN-Lf?usp=sharing

Lembrado que o bot tem que estar no servidor com esse emojis.
Como pegar o id do emoji? 
1° adcione no servidor
2° vá no discord e digite    \ e selecione o emoji . Ai ele irá retornár um o id  exemplo : <:support:439639384418025475>
3° agora so trocar os emojis no codigo pelos do seu servidor.


LEMBRANDO
    -OS NOMES DO CARGOS TEM QUE SER INDÊNTICO AO DO SERVIDOR
    -E PRA ADD CUSTO REACTION NA MESSAGEM NÃO PODE TER OS < >

"""

@client.event
async def on_message(message):
    if message.content.lower().startswith("py_lol"):
        embedlol = discord.Embed(
            title='Escolha Seu Elo e Lane',
            color=COR,
            description='\n'
                        '\n')

        embedlol.set_thumbnail(url='https://i.imgur.com/Mn08hTd.png')
        embedlol.add_field(name='Unranked', value='<:unraked:439639400666759180>', inline=True)
        embedlol.add_field(name='Top', value='<:top:439639384573214742>', inline=True)
        embedlol.add_field(name='Bronze', value='<:bronze:439639385017942036>', inline=True)
        embedlol.add_field(name='Jungle', value='<:jungle:439639384036474881>', inline=True)
        embedlol.add_field(name='Prata', value='<:prata:439639397001068544>', inline=True)
        embedlol.add_field(name='Mid', value='<:mid:439639384128618506>', inline=True)
        embedlol.add_field(name='Ouro', value='<:ouro:439639401685843987>', inline=True)
        embedlol.add_field(name='Adc', value='<:adc:439639377212080129>', inline=True)
        embedlol.add_field(name='Platina', value='<:platina:439639389900111872>', inline=True)
        embedlol.add_field(name='Suporte', value='<:support:439639384418025475>', inline=True)
        embedlol.add_field(name='Diamante', value='<:diamante:439639397273436160>', inline=True)
        botmsg = await client.send_message(message.channel, embed=embedlol)

        await client.add_reaction(botmsg, ":unraked:439639400666759180")
        await client.add_reaction(botmsg, ":bronze:439639385017942036")
        await client.add_reaction(botmsg, ":prata:439639397001068544")
        await client.add_reaction(botmsg, "::ouro:439639401685843987")
        await client.add_reaction(botmsg, ":platina:439639389900111872")
        await client.add_reaction(botmsg, ":diamante:439639397273436160")
        await client.add_reaction(botmsg, ":top:439639384573214742")
        await client.add_reaction(botmsg, ":jungle:439639384036474881")
        await client.add_reaction(botmsg, ":mid:439639384128618506")
        await client.add_reaction(botmsg, ":adc:439639377212080129")
        await client.add_reaction(botmsg, ":support:439639384418025475")

        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.custom_emoji and reaction.emoji.id == "439639400666759180":
     role = discord.utils.find(lambda r: r.name == "● Unranked", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639385017942036":
     role = discord.utils.find(lambda r: r.name == "● Bronze", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639397001068544":
     role = discord.utils.find(lambda r: r.name == "● Prata", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639401685843987":
     role = discord.utils.find(lambda r: r.name == "● Gold", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639389900111872":
     role = discord.utils.find(lambda r: r.name == "● Platina", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639397273436160":
     role = discord.utils.find(lambda r: r.name == "● Diamante", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384573214742":
     role = discord.utils.find(lambda r: r.name == "● Top", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384036474881":
     role = discord.utils.find(lambda r: r.name == "● Jg", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384128618506":
     role = discord.utils.find(lambda r: r.name == "● Mid", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639377212080129":
     role = discord.utils.find(lambda r: r.name == "● Adc", msg.server.roles)
     await client.add_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384418025475":
     role = discord.utils.find(lambda r: r.name == "● Suporte", msg.server.roles)
     await client.add_roles(user, role)


@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    if reaction.custom_emoji and reaction.emoji.id == "439639400666759180":
     role = discord.utils.find(lambda r: r.name == "● Unranked", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639385017942036":
     role = discord.utils.find(lambda r: r.name == "● Bronze", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639397001068544":
     role = discord.utils.find(lambda r: r.name == "● Prata", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639401685843987":
     role = discord.utils.find(lambda r: r.name == "● Gold", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639389900111872":
     role = discord.utils.find(lambda r: r.name == "● Platina", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639397273436160":
     role = discord.utils.find(lambda r: r.name == "● Diamante", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384573214742":
     role = discord.utils.find(lambda r: r.name == "● Top", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384036474881":
     role = discord.utils.find(lambda r: r.name == "● Jg", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384128618506":
     role = discord.utils.find(lambda r: r.name == "● Mid", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639377212080129":
     role = discord.utils.find(lambda r: r.name == "● Adc", msg.server.roles)
     await client.remove_roles(user, role)
    if reaction.custom_emoji and reaction.emoji.id == "439639384418025475":
     role = discord.utils.find(lambda r: r.name == "● Suporte", msg.server.roles)
     await client.remove_roles(user, role)




client.run('seu_token_aqui')
