import discord
from discord.ext import commands
import os
import time
import re
import asyncio

''' VARIAVEIS'''
ownerid = '232309115865661440'
bot = commands.Bot(command_prefix='p!', description='pythonzinho')
bot.remove_command('help')
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:

    token = 'token aqui'

user = discord.Member
''' EVENTOS DO BOT'''

@bot.event
async def on_ready():
    print('Logado em')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='p!ajuda'))




''' COMANDOS DO BOT'''
# Ban
@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        await bot.ban(member)
        await bot.say("{} Banido".format(member.mention))
    else:
        embed = discord.Embed(title=":x: Erro!", description=" \n ", color=0xff0000)
        embed.add_field(name="<:err:439106887829553173>{} Permissão insuficiente!".format(
            ctx.message.author.name), value='_Ban Ban_', inline=False)
        embed.set_thumbnail(url=member.avatar_url)

        await bot.say(embed=embed)

# ADD CARGO
@bot.command()
async def addcargo(ctx, member: discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
        return await bot.say("<:err:439106887829553173> Permissão insuficiente!")
    try:
       await bot.add_roles(member, role_name)
       await bot.say(" Cargo {} Adcionado para : {}.".format(role_name, member.name))
    except discord.ext.commands.errors.MissingRequiredArgument as e:
       await  bot.say('<:err:439106887829553173> {}'.format(e))



# REMOVER CARGO
@bot.command(pass_context=True)
async def removecargo(ctx, member: discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
        return await bot.say("<:err:439106887829553173> Permissão insuficiente!")
    await bot.remove_roles(member, role_name)
    await bot.say(" Cargo {} Removido de {}.".format(role_name, member.name))


# DESMULTAR O USUARIO
@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    if not ctx.message.author.server_permissions.administrator:
        return await bot.say("<:err:439106887829553173> Permissão insuficiente!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await bot.say("" + member.mention + " foi desmultado ")
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)


#IMPEDIR DO USUÁRIO DIGITAR POR UM PERIODO DE TEMPO
@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member, mutetime):
    if not ctx.message.author.server_permissions.administrator:
        return await bot.say("<:err:439106887829553173> Permissão insuficiente!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await bot.say("" + member.mention + " foi mutado por " + mutetime + " minutos !")
    await asyncio.sleep(int(mutetime))
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)



# RENOMEAR O NICK DO USUARIO
@bot.command(pass_context=True)
async def renomear(ctx, membro: discord.Member, *, nick=""):
    await bot.delete_message(ctx.message)
    if not ctx.message.author.server_permissions.administrator:
        return await bot.say("<:err:439106887829553173> Permissão insuficiente!")
    nickantigo = membro.display_name
    await bot.change_nickname(membro, nick)
    embedren = discord.Embed(title=" Alteração de nick!", description=" \n ", color=0x2df700)
    embedren.set_thumbnail(url=membro.avatar_url)
    embedren.add_field(name='Antigo nick', value=nickantigo, inline=True)
    embedren.add_field(name='Novo nick', value=nick, inline=True)
    embedren.add_field(name='Alterado por', value=ctx.message.author, inline=True)
    await bot.say(embed=embedren)


# KIKA UM MEMBRO DO SERVE
@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        await bot.say("Kikado!")
        await bot.kick(member)
    else:
        embed = discord.Embed(title=":x: Error!", description=None, color=0x2df700)
        embed.add_field(name="Voce nao possui perrmissão para esse comando procure um administrador.".format(
            ctx.message.author.name), value='_Membro kikado_', inline=False)
        embed.set_thumbnail(url=member.avatar_url)

        await bot.say(embed=embed)



# DELETA MENSAGENS
@bot.command(pass_context=True)
async def delete(ctx, number):
    if not ctx.message.author.server_permissions.manage_messages:
        return await bot.say("<:err:439106887829553173>Permissão insuficiente.")
    elif int(number) > 100:
        return await bot.say("<:err:439106887829553173> O limite é 100.")
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    await bot.say("  Deletado `{}` messages.".format(number))


#ALTERA o STATUS DO BOT
@bot.command(pass_context=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id == (ownerid):
        await bot.whisper("Status alterado para **{}**!".format(game))
        await bot.change_presence(game=discord.Game(name=game))
    else:
        await bot.say("<:err:439106887829553173> Permissão insuficiente!")


#INFO DO BOT
@bot.command(pass_context=True)
async def botinfo():
    github ='https://github.com/vagner2k18/pythozinho'
    invite ='https://discordapp.com/oauth2/authorize?client_id=420703371918442499&permissions=2146958583&scope=bot'
    supp='https://discord.gg/brQfChz'
    embedbotin = discord.Embed(title="<:info:439189290078044160> Olá sou pythozinho", description="Um Simples bot para discord", color=0x2df700)
    embedbotin.add_field(name='ﾠ', value='<:314003252830011395:433479573473067010> Status\n',inline=False)
    embedbotin.add_field(name='<:cpu:438098135429021696> Servidores', value='`{}`'.format(str(len(bot.servers))),inline=True)
    embedbotin.add_field(name='👥 Usuarios', value='`{}`'.format(len(set(bot.get_all_members()))),inline=True)
    embedbotin.add_field(name='💬 Canais', value='`{}`'.format(len(set(bot.get_all_channels()))),inline=True)
    embedbotin.add_field(name='ﾠ', value='🔗 Links',inline=False)
    embedbotin.add_field(name='<:git:439158607318089740> GitHub', value='[**link**](' + github + ')\n',inline=True)
    embedbotin.add_field(name='<:invite:439158621306093578> Convite', value='[**link**](' + invite + ')\n',inline=True)
    embedbotin.add_field(name='<:gear:439186818433286144> Support', value='[**link**](' + supp + ')\n',inline=True)
    embedbotin.set_footer(text="Copyright © 2018 vagner")
    await bot.say(embed=embedbotin)

#REPETE O FOI DITO
@bot.command(pass_context=True)
async def diz(self, *, msg: str):
    await bot.delete_message(self.message)
    msg = re.sub('´', '`', msg)
    await self.bot.say(msg)

# GERA CONVITE
@bot.command(pass_context=True)
async def convite(ctx):
    invite = await bot.create_invite(ctx.message.channel, max_uses=1, xkcd=True)
    await bot.send_message(ctx.message.author, "📬 Convite gerado. Link : {}".format(invite.url))


# COMANDO PING PONG
@bot.command(pass_context=True)
async def ping(ctx):
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    pingtime = time.time()
    ping = time.time() - pingtime
    pingembed = discord.Embed(title='<:net:439123684997857301>Connection Status <:net:439123684997857301>',description=None,color=0x2df700)
    pingembed.set_thumbnail(url='https://i.imgur.com/6cefaMv.png')
    #pingembed.add_field(name='<:cpu:438098135429021696>  **Response time with server**',value='`%.01f seconds`' % ping,inline=False)
    pingembed.add_field(name='<:313956277107556352:433479570277138432>  **Latency**',value='`{} ms`'.format(round((t2-t1)*1000)),inline=False)
    pingembed.set_footer(text="Copyright © 2018 vagner")
    await bot.say(embed=pingembed)


@bot.command(pass_context=True)
async def ajuda(ctx):
    embedajuda = discord.Embed(title="Sou apenas um simples bot de moderação criado para meu servidor", description="Abaixo segue meus comandos",color=0x2df700)
    embedajuda.set_thumbnail(url='https://i.imgur.com/oFwDf4p.png')
    embedajuda.add_field(name='**⚖️ MODERAÇÃO**', value="`p!setgame`\n`p!delete`\n`p!ban`\n`p!addcargo`\n`p!removecargo`\n`p!mute`\n`p!unmute`\n`p!renomear`\n`p!kick`", inline=True)
    embedajuda.add_field(name='**💻 ULTILIDADEs**', value='`p!botinfo`\n`p!diz`\n`p!convite`',inline=True)
    embedajuda.set_footer(text="created by vagner")
    await bot.send_message(ctx.message.author, embed=embedajuda)


'''TOKEN PARA RODAR BOT'''
bot.run(token)