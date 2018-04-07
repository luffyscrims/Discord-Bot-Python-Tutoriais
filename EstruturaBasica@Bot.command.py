'''IMPORTAÇOES BASICAS'''
import discord
from discord.ext import commands
import os


'''VARIAVEIS'''
#Aqui fica o prefixo que inicia o comando no discord
bot = commands.Bot(command_prefix='?', description='Bem vindos Ao discord.')
client = discord.Client()
#parte para esconder seu token quando for mandar para o github
#lembre de criar um arquivo secreto.py pra colocar seu token
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

'''EVENTOS DO BOT'''
@bot.event
#aqui mostra no terminal onde o bot ta logado e muda o status de online do bot no discord
async def on_ready():
    print('Logado em')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    return await bot.change_presence(game=discord.Game(name='Digite aqui os status do bot'))

'''COMANDOS DO BOT'''
#ao digitar o prefixo com a variavel depois do async def EX: ?test
#o bot irá exibir no discord Olá Mundo
@bot.command()
async def test():
     await bot.say('Olá Mundo!')


'''TOKEN PARA RODAR BOT'''
#aqui é a parte final para roda o bot
#o token mesmo fica no secreto.py
#essa forma é para que o token do seu bot
#nao fique exposto
bot.run(token)
