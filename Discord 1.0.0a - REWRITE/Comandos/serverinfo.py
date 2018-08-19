import discord

#declaração do client e o prefixo
client = discord.Client()
prefixo = "t!"

#evento de login do bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='vagner tutorial', type=discord.ActivityType.playing))
    print("----------ONLINE")
    print(client.user.name)
    print(client.user.id)
    print(f"Em  {str(len(client.guilds))} Servidores")
    print(f'Em contato com {str(len(set(client.get_all_members())))} usuarios')
    print("---------")


#evento de message do bot
@client.event
async def on_message(message):
    if message.content.lower().startswith(prefixo+"serverinfo"):
        embedtest = discord.Embed(title='Server Info',color=0x83f68a,description=message.guild.name)
        embedtest.add_field(name="Id",value=message.guild.id)
        embedtest.add_field(name="Cargos", value=len(message.guild.roles))
        embedtest.add_field(name="Membros", value=message.guild.member_count)
        embedtest.add_field(name="Criado em", value=message.guild.created_at.strftime("%d %b %Y %H:%M"))
        embedtest.add_field(name="Região", value=message.guild.region)
        embedtest.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embedtest)

client.run("toke aqui")