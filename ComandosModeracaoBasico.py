#Importação basica
import discord


#Variavel para uso do discord
client = discord.Client()

#Evento de loggin do bot
@client.event
async def on_ready():
    print("----Tutorial modecação-----")
    print("Nome do bot{}".format(client.user.name))
    print("Logado em {} servidores".format(len(client.servers)))
    print("---Tutorial By vagner----")
    print("---Lado Nego----")
    await client.change_presence(game=discord.Game(name="prefixo !",type= 1))
    


#Evento de messagem do bot
@client.event
async def on_message(message):
    if message.content.lower().startswith("!ban"):
      try:
        #Vai verificar se quem usou o comando tem permissão de adm   
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        author = message.author.mention
        user = message.mentions[0]
        await client.ban(user)
        await client.send_message(message.channel,"Usuario: {} banido do server pelo Administrador: {}".format(user.mention,author))
       #no caso do membro mencionado ser um adm vai enviar uma messagem
      except  discord.errors.Forbidden:
          return await client.send_message(message.channel, '⚠️ Nao posso banir o administrador :{}'.format(user.mention))



    if message.content.lower().startswith("!mute"):
        #vai verificar se quem usou o comando possui permissão de adm
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        author= message.author.mention
        user = message.mentions[0]
        """Lembrando que tem que ter o cargo mutado no seu server"""
        """Lembrando que vc tem que retirar todas permissões do cargo mutado"""
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi mutado pelo Administrador: {}'.format(user.mention,author))

    if message.content.lower().startswith("!desmultar"):
        # vai verificar se quem usou o comando possui permissão de adm
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        author = message.author.mention
        user = message.mentions[0]
        """Lembrando que tem que ter o cargo mutado no seu server"""
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi Desmultado pelo Administrador: {}'.format(user.mention, author))

#CASO TENHA ALGUM ERRO NO CODIGO. ENTRE NO SERVIDOR LADO NEGRO IREMOS TE AJUDAR
#AQUI VAI SEU TOKEN

client.run('INSIRA SEU TOKEN AQUI')
