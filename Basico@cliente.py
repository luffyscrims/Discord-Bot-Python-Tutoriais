#importaçoes Basicas
import discord



#Variavél para poder usar @client
client = discord.Client()
COR = '#4286f4'#
#montra no terminal se deu certo no loggin do bot,e muda os status do bot no discord
@client.event
async def on_ready():
    print("Bot logado")
     await client.change_presence(game=discord.Game(name="League of legends", url="https://www.twitch.tv/vagner8k", type=1))


#parte dos comandos alguns exemplos com imagens e embedd
@client.event
async def on_message(message):
     if message.content.lower().startswith('!teste'):
        embedvagner = discord.Embed(
            title='bla bla',
            color=0x83f68a,
            description='bla bla'
        )
        embedvagner.add_field(name='ola', value='oi')
        embedvagner.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embedvagner)
    
    if message.content.lower().startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong" % (userID))

    if message.content.lower().startswith('?img'):
        embed = discord.Embed(color=COR)
        embed.set_image(
            url="https://i.imgur.com/wZvT6CH.jpg")
        await client.send_message(message.channel, embed=embed)

    
#insira o token do bot aqui entre as aspas simples
client.run('token aki')
