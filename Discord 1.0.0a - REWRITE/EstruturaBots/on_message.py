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
    if message.content.lower().startswith(prefixo+"embed"):
        argumento = message.content[7:]
        if not argumento:
            await message.channel.send("**Insira um texto para colocar no embed**")
            return
        embedtest = discord.Embed(title='Embed Basico',color=0x83f68a,description=None)
        embedtest.add_field(name="Campo 1",value=argumento)
        embedtest.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embedtest)

client.run("Token aqui")
