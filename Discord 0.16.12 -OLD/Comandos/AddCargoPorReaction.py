import discord
import random


COR = 0x690FC3
msg_id = None
msg_user = None



client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE !')
    print(client.user.name)
    print(client.user.id)
    print('-----Tutorial ADD roles-----')

@client.event
async def on_message(message):

    if message.content.lower().startswith('-test'):
        await client.send_message(message.channel, "Olá Mundo, Estou Vivo!")

    if message.content.lower().startswith('-moeda'):
     choice = random.randint(1,2)
     if choice == 1:
         await client.add_reaction(message, '😀')
     if choice == 2:
         await client.add_reaction(message, '👑')

    if message.content.lower().startswith("-game"):
     embed1 =discord.Embed(

        title="Escolha seu elo!",
        color=COR,
        description="- Bronze = 🥉\n"
                    "- Prata =  🥈 \n"
                    "- Ouro  = 🥇",)
     botmsg = await client.send_message(message.channel, embed=embed1)

     await client.add_reaction(botmsg, "🥉")
     await client.add_reaction(botmsg, "🥈")
     await client.add_reaction(botmsg, "🥇")

     global msg_id
     msg_id = botmsg.id
     global msg_user
     msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
#Lembrado que tem que te o cargo no seu servidor    
    if reaction.emoji == "🥉" and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "BRONZE", msg.server.roles)
     await client.add_roles(user, role)


    if reaction.emoji == "🥈"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "PRATA", msg.server.roles)
     await client.add_roles(user, role)


    if reaction.emoji == "🥇"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "OURO", msg.server.roles)
     await client.add_roles(user, role)


@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🥉" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "BRONZE", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🥈"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "PRATA", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🥇" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "OURO", msg.server.roles)
     await client.remove_roles(user,role)


client.run('Bote seu token aqui')
