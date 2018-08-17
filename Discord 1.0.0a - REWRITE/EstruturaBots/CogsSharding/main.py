import discord
from discord.ext import commands
import json


#vamos abrir o setup json para pegar as informaçoes
with open('bot_setup.json') as vagner:
    bot_settings =json.load(vagner)

#lista de comandos
# cmds.info  o cmds que dizer o nome da pastar e o info o nome do arquivo
#pode fazer tbm cmds.adm.ban  caso queria deixar mais organizado a cada . entra em um diretorio
cmd_open=['cmds.info']


#vamos criar o setup do bot
class main(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=bot_settings['prefixo'],
                         description="tutorial Cogs Rewritre",
                         pm_help=None,
                         #aqui iremos definir a quantidade de shards
                         shard_count=bot_settings['shard_count'])
        self.token = bot_settings['token']
        #Aqui é para remover aquele help padrão mo feio
        self.remove_command('help')

    #agora vamos ao eventos do bot
    async def on_ready(self):
        #carregar os comandos
        for extension in cmd_open:
            try:
                bot.load_extension(extension)
                print(f"Comando {extension} carregado com sucesso")
            except Exception as e:
                exc = '{}.{}'.format(type(e).__name__, e)
                print('falha ao carregar extensoes {} . {} detalhes {}'.format(extension, e,exc))

        await self.change_presence(activity=discord.Activity(name='tutorial vagner',type=discord.ActivityType.listening))
        print("Logado.")

    async def on_message(self,message):
        #vamos bloquear o bot para n responder a bots
        if message.author.bot:
            pass
        #vamos impedir comandos via dm
        elif isinstance(message.channel, discord.abc.GuildChannel) is False:
            return
        else:
            await bot.process_commands(message)

    #funcão para logar o bot
    def run(self):
        super().run(bot.token, reconnect=True)


if __name__ =="__main__":
 bot = main()
 bot.run()

