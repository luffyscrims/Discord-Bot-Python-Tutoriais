# -*- coding: utf-8 -*-
"""
Sesshomaru v(1.0.0)
~~~~~~~~~~~~~~~~~~~
Full code .
:copyright: (c) 2019 Vagner
:license: MIT .
"""


#  ___                                      _
# |_ _|  _ __ ___    _ __     ___    _ __  | |_   ___
#  | |  | '_ ` _ \  | '_ \   / _ \  | '__| | __| / __|
#  | |  | | | | | | | |_) | | (_) | | |    | |_  \__ \
# |___| |_| |_| |_| | .__/   \___/  |_|     \__| |___/
#                   |_|
import discord
import asyncio
import random
import psutil
import random as r
from time import sleep as s
import time, datetime
import requests
import io
import safygiphy
import json
import os
from googletrans import Translator

# __     __                 _                          _
# \ \   / /   __ _   _ __  (_)   __ _  __   __   ___  (_)  ___
#  \ \ / /   / _` | | '__| | |  / _` | \ \ / /  / _ \ | | / __|
#   \ V /   | (_| | | |    | | | (_| |  \ V /  |  __/ | | \__ \
#    \_/     \__,_| |_|    |_|  \__,_|   \_/    \___| |_| |___/

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
    fort_key = os.environ.get('FORT_KEY')
else:
    
    token = "token aqui"
    fort_key = "fortnite key aqui"

msg_id = None
g = safygiphy.Giphy()
start_time = int(time.time())
version = 'Beta'
client = discord.Client()
RED = "#000000"
minutes = 0
hour = 0
onwer = ['232309115865661440']


#  _        ___     ____     _               _        ___
# | |      / _ \   / ___|   | |__     ___   | |_     / _ \   _ __
# | |     | | | | | |  _    | '_ \   / _ \  | __|   | | | | | '_ \
# | |___  | |_| | | |_| |   | |_) | | (_) | | |_    | |_| | | | | |
# |_____|  \___/   \____|   |_.__/   \___/   \__|    \___/  |_| |_|

@client.event
async def on_ready():
    print("=================================")
    print(f"Nome:{client.user.name}")
    print(f"ID: {client.user.id}")
    print("On line em : {} Serves".format(str(len(client.servers))))
    print('Users ' + str(len(set(client.get_all_members()))) + ' usuarios')
    print(f"Bot Versão: {version}")
    print("=================================")
    await client.change_presence(game=discord.Game(name="s!ajuda "))


#  _        ___     ____   ____      ____
# | |      / _ \   / ___| / ___|    / ___|    ___   _ __  __   __   ___   _ __
# | |     | | | | | |  _  \___ \    \___ \   / _ \ | '__| \ \ / /  / _ \ | '__|
# | |___  | |_| | | |_| |  ___) |    ___) | |  __/ | |     \ V /  |  __/ | |
# |_____|  \___/   \____| |____/    |____/   \___| |_|      \_/    \___| |_|


@client.event
async def on_member_remove(member):
    if member.server.id == '299626669336035330':
        channel = client.get_channel("439520276342898688")
        msg = "🏃‍️{0} ,Saiu do {1} server!".format(member.mention, member.server.name)
        await client.send_message(channel, msg)


@client.event
async def on_member_join(member):
    if member.server.id == '299626669336035330':
        channel = client.get_channel("439520276342898688")
        msg = "🕺 Bem Vindo {0} ao {1} server!".format(member.mention, member.server.name)
        await client.send_message(channel, msg)


@client.event
async def on_server_join(server):
    log_server = client.get_server('299626669336035330')
    log_channel = discord.utils.get(log_server.channels, name='log-server-on')
    await client.send_message(log_channel, '✅ Entrei no server {}'.format(server.name))


@client.event
async def on_server_remove(server):
    log_server = client.get_server('299626669336035330')
    log_channel = discord.utils.get(log_server.channels, name='log-server-on')
    await client.send_message(log_channel, '⛔️ fui removido do server {}'.format(server.name))


@client.event
async def on_error(event, *args, **kwargs):
    log_server = client.get_server('299626669336035330')
    log_channel = discord.utils.get(log_server.channels, name='log-error')
    await client.send_message(log_channel, f'ERROR: Evento {event}\n args {args}\n Kwargs{kwargs}')


@client.event
async def on_message(message):
    #  __  __    ___    ____      ____
    # |  \/  |  / _ \  |  _ \    / ___|    ___   _ __  __   __   ___   _ __
    # | |\/| | | | | | | | | |   \___ \   / _ \ | '__| \ \ / /  / _ \ | '__|
    # | |  | | | |_| | | |_| |    ___) | |  __/ | |     \ V /  |  __/ | |
    # |_|  |_|  \___/  |____/    |____/   \___| |_|      \_/    \___| |_|

    if message.channel == client.get_channel('426043453756014592'):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    elif message.author.bot:
        pass

    elif message.content.lower().startswith('<@425670256741187604>'):
        await client.send_message(message.channel, "<:sesho:433317803328536576>use `s!ajuda` para ver meus comandos.")

    #   ____                                           _                 _               _        _               _
    #  / ___|   ___    _ __ ___     __ _   _ __     __| |   ___       __| |   ___       / \      (_)  _   _    __| |   __ _
    # | |      / _ \  | '_ ` _ \   / _` | | '_ \   / _` |  / _ \     / _` |  / _ \     / _ \     | | | | | |  / _` |  / _` |
    # | |___  | (_) | | | | | | | | (_| | | | | | | (_| | | (_) |   | (_| | |  __/    / ___ \    | | | |_| | | (_| | | (_| |
    #  \____|  \___/  |_| |_| |_|  \__,_| |_| |_|  \__,_|  \___/     \__,_|  \___|   /_/   \_\  _/ |  \__,_|  \__,_|  \__,_|
    #                                                                                          |__/
    elif message.content.lower().startswith('s!ajuda'):
        try:
            await client.delete_message(message)
            await client.send_message(message.channel, "<:sesho:433317803328536576> Enviei meus comandos no Dm!")
            embedhelp = discord.Embed(
                title=None,
                color=0x1CF9FF,
                description=None)
            embedhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
            embedhelp.add_field(name='**COMANDOS**', value='📜 Formato on_message', inline=True)
            embedhelp.add_field(name='**TOTAL**', value='`47 COMANDOS`', inline=False)
            embedhelp.add_field(name='**SOBRE**',
                                value='`Sou apenas um simples bot para discord\nCriado pelo pelo Vagner\nVersão: 2.1`',
                                inline=False)
            embedhelp.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            rr = await client.send_message(message.author, embed=embedhelp)
            await client.add_reaction(rr, '📜')
            await client.add_reaction(rr, '🔐')
            await client.add_reaction(rr, '🔍')
            await client.add_reaction(rr, '🎉')
            await client.add_reaction(rr, '📖')
            await client.add_reaction(rr, '⚙')

            global msg_id
            msg_id = rr.id
            global msg_user
            msg_user = message.author
        except:
            await client.send_message(message.channel, '<:sesho:433317803328536576> Seu DM está desativado!')
    # __     __                                          ____            _           _   _                                   _
    # \ \   / /   __ _    __ _   _ __     ___   _ __    | __ )    ___   | |_      __| | (_)  ___    ___    ___    _ __    __| |
    #  \ \ / /   / _` |  / _` | | '_ \   / _ \ | '__|   |  _ \   / _ \  | __|    / _` | | | / __|  / __|  / _ \  | '__|  / _` |
    #   \ V /   | (_| | | (_| | | | | | |  __/ | |      | |_) | | (_) | | |_    | (_| | | | \__ \ | (__  | (_) | | |    | (_| |
    #    \_/     \__,_|  \__, | |_| |_|  \___| |_|      |____/   \___/   \__|    \__,_| |_| |___/  \___|  \___/  |_|     \__,_|
    #                    |___/

    #  _           __  __               _
    # / |         |  \/  |   ___     __| |   ___   _ __    __ _    ___    __ _    ___
    # | |  _____  | |\/| |  / _ \   / _` |  / _ \ | '__|  / _` |  / __|  / _` |  / _ \
    # | | |_____| | |  | | | (_) | | (_| | |  __/ | |    | (_| | | (__  | (_| | | (_) |
    # |_|         |_|  |_|  \___/   \__,_|  \___| |_|     \__,_|  \___|  \__,_|  \___/

    # HELP MODERAÇAO
    elif message.content.lower().startswith("s!modhelp"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,
                                             "⚠ {} Voçe nao possui permissão!".format(message.author.mention))
        # await client.delete_message(message)
        modhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='🔐Comandos de Moredação🔐 ')
        modhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        modhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        modhelp.add_field(name='**s!getban**', value='`Retorna todos os membros banidos do servidor`', inline=False)
        modhelp.add_field(name='**s!changegame**',
                          value='`<status em texto> Muda o status to bot para o que foi passado no parametro`',
                          inline=False)
        modhelp.add_field(name='**s!apagar**',
                          value='`<quantidade em inteiro> Deleta messagens pela quantidante passada ,Não possui limite`',
                          inline=False)
        modhelp.add_field(name='**s!ban**', value='`<menção do usuario> Bane o usuario do servidor`', inline=False)
        modhelp.add_field(name='**s!ban2**', value='`<menção do usuario> Bane o usuario do servidor. Visual melhorado`',
                          inline=False)
        modhelp.add_field(name='**s!mute**',
                          value='`<menção do usuario> Adiciona o cargo mutado ao memmbro mencionado`', inline=False)
        modhelp.add_field(name='**s!desmultar**',
                          value='`<menção do usuario> Remove o cargo mutado ao memmbro mencionado`', inline=False)
        modhelp.add_field(name='**s!sban**',
                          value='`<menção do usuario>+<motivo em texto> Bane o usuario do servidor é mostra o motivo`',
                          inline=False)
        modhelp.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                           icon_url=message.author.avatar_url)
        mod = await client.send_message(message.author, embed=modhelp)
        await asyncio.sleep(30)
        await client.delete_message(mod)

    # COMANDO 1.1
    elif message.content.lower().startswith("s!getban"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,
                                             "⚠ {} Voçe nao possui permissão!".format(message.author.mention))
        # await client.delete_message(message)
        await client.send_typing(message.channel)
        try:
            banlist = await client.get_bans(message.server)
            if len(banlist) == 0:
                await client.send_message(message.channel, "⚠ Esse sever não possui usuarios banidos")
            else:
                banlist1 = discord.Embed(title='`Banimentos do servidor {}`'.format(message.server.name),
                                         color=0x1CF9FF, description=None)

                await client.send_message(message.channel, embed=banlist1)
                for b in banlist:
                    responses = "{}".format(b)

                    banlist = discord.Embed(title=None,
                                            color=0x1CF9FF, description=responses)

                    await client.send_message(message.channel, embed=banlist)
        except discord.errors.Forbidden:
            ban = await client.send_message(message.channel, '⚠ Sem permissão de ver banimentos desse servidor')
            await asyncio.sleep(10)
            await client.delete_message(ban)
        except Exception as e:
            await client.send_message(message.channel, 'Ocorreu um error : {}'.format(e))


    # COMANDO 1.2
    elif message.content.lower().startswith('s!ban2'):
        # await client.delete_message(message)
        membro = message.mentions[0]
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,
                                             "⚠ {} Voçe nao possui permissão!".format(message.author.mention))

        await client.send_message(message.channel, "{} Baniu {} com sucesso.".format(message.author.mention,
                                                                                     message.mentions[0].mention))
        await client.ban(membro)



    # COMANDO 1.3
    elif message.content.startswith("s!changegame"):
        # await client.delete_message(message)
        gameName = message.content.replace("s!changegame", "")
        if message.author.server_permissions.administrator:
            await client.change_presence(game=discord.Game(name=gameName))
            await client.send_message(message.channel, "`Status bot alterado para: {}`".format(gameName))
        else:
            await client.send_message(message.channel, "⚠  Somente ADM podem mudar meus Status")


    # COMANDO 1.4
    elif message.content.lower().startswith('s!apagar'):
        # await client.delete_message(message)
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️ Permissão insuficiente')
        lim = int(message.content[8:])
        await client.purge_from(message.channel, limit=lim)
        purge = await client.send_message(message.channel,
                                          " foi deletado: {} msgs por {}".format(lim, message.author.mention))
        await asyncio.sleep(10)
        await client.delete_message(purge)

    # COMANDO 1.5
    elif message.content.lower().startswith("s!ban"):
        # await client.delete_message(message)
        try:

            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel, '⚠️Permissão insuficiente')
            author = message.author.mention
            user = message.mentions[0]
            await client.ban(user)
            await client.send_message(message.channel,
                                      "Usuario: {} banido do server pelo Administrador: {}".format(user.mention,
                                                                                                   author))
        except  discord.errors.Forbidden:
            return await client.send_message(message.channel,
                                             '⚠️ Nao posso banir o administrador :{}'.format(user.mention))

    # COMANDO 1.6
    elif message.content.lower().startswith("s!mute"):
        # await client.delete_message(message)
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        author = message.author.mention
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel,
                                  'O membro: {} foi mutado pelo Administrador: {}'.format(user.mention, author))

    # COMANDO 1.7
    elif message.content.lower().startswith("s!desmultar"):
        #  await client.delete_message(message)
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        author = message.author.mention
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel,
                                  'O membro: {} foi Desmultado pelo Administrador: {}'.format(user.mention, author))


    # COMANDO 1.8
    elif message.content.lower().startswith("s!sban"):
        #  await client.delete_message(message)
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '⚠ Voçe nao possui  permissão')
        reason = ' '.join(message.content.split(' ')[2::])
        try:
            user = message.mentions[0]
            await client.ban(user)
            if user != None:
                await client.send_message(message.channel,
                                          'Membro : {} Foi Banido. Motivo: {}'.format(user.mention, reason))
            else:
                await message.author.send('Id invalido')
        except discord.HTTPException:
            pass
        finally:
            pass

    # COMANDO 1.9
    elif message.content.startswith('s!update'):
        if not message.author.id == '232309115865661440':
            return await client.send_message(message.channel, '⚠ Voçe nao possui  permissão')
        mensagem = message.content[9:]
        canal = discord.utils.find(lambda c: c.name == 'anuncios', message.server.channels)
        em = discord.Embed(description=mensagem, colour=0xdb513a)
        em.set_author(name='Novidades!', icon_url=message.author.avatar_url)
        em.set_footer(text='Att.{}, Developer Zone.'.format(message.author.name))
        await client.send_message(canal, '@everyone', embed=em)



    #  _____   _____   _____   _____   _____   _____   _____   _____   _____
    # |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

    #  ____            ____                                 _
    # |___ \          / ___|    ___    __ _   _ __    ___  | |__
    #   __) |  _____  \___ \   / _ \  / _` | | '__|  / __| | '_ \
    #  / __/  |_____|  ___) | |  __/ | (_| | | |    | (__  | | | |
    # |_____|         |____/   \___|  \__,_| |_|     \___| |_| |_|

    # HELP SEARCH
    elif message.content.lower().startswith("s!searchhelp"):
        # await client.delete_message(message)
        searchhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='🔍Comandos de Search🔍')
        searchhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        searchhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        searchhelp.add_field(name='**s!google**', value='`<pesquisa em texto> Faz uma busca no google`', inline=False)
        searchhelp.add_field(name='**s!youtube**', value='`<pesquisa em texto> Faz uma busca no youtube`', inline=False)
        searchhelp.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        search = await client.send_message(message.author, embed=searchhelp)
        await asyncio.sleep(30)
        await client.delete_message(search)


    # COMANDO 2.1
    elif message.content.lower().startswith("s!google"):
        #  await client.delete_message(message)
        words = 'https://www.google.com/search?q=' + message.content[8:].strip().replace(' ', '+')
        await client.send_message(message.channel, words)

    # COMANDO 2.2
    elif message.content.lower().startswith("s!youtube"):
        #  await client.delete_message(message)
        words = 'https://www.youtube.com/results?search_query=' + message.content[9:].strip().replace(' ', '+')
        await client.send_message(message.channel, words)


    #  _____   _____   _____   _____   _____   _____   _____   _____   _____
    # |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

    #  _____           _   _   _     _   _
    # |___ /          | | | | | |_  (_) | |  ___
    #   |_ \   _____  | | | | | __| | | | | / __|
    #  ___) | |_____| | |_| | | |_  | | | | \__ \
    # |____/           \___/   \__| |_| |_| |___/
    # HELP UTILS
    elif message.content.lower().startswith("s!utilshelp"):
        # await client.delete_message(message)
        utilshhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='⚙Comandos Utils⚙')
        utilshhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        utilshhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        utilshhelp.add_field(name='**s!convite**', value='`Gera o convite do servidor`', inline=False)
        utilshhelp.add_field(name='**s!feedback**', value='`Envia um feedback para meu desenvolvedor`', inline=False)
        utilshhelp.add_field(name='**s!py**', value='`<codigo em texto> Formata seu codigo para python`', inline=False)
        utilshhelp.add_field(name='**s!js**', value='`<codigo em texto> Formata seu codigo para javascript`',
                             inline=False)
        utilshhelp.add_field(name='**s!hora**', value='`Retorna a hora atual`', inline=False)
        utilshhelp.add_field(name='**s!jogo**',
                             value='`<status em texto> Altera meu status para.Somente meu criador pode usar no momento`',
                             inline=False)
        utilshhelp.add_field(name='**s!votar**', value='`<texto>Enviar seu texto para o servidor em forma de votação`',
                             inline=False)
        utilshhelp.add_field(name='**s!membro**', value='`Para ganhar o cargo membro no servidor`', inline=False)
        utilshhelp.add_field(name='**s!tr**', value='`<texto><linguagem> Traduz o texto passado`', inline=False)
        utilshhelp.add_field(name='**s!aviso**',
                             value='`<aviso em texto>Envia o texto em formar de aviso para o canal atual`',
                             inline=False)
        utilshhelp.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        utils = await client.send_message(message.author, embed=utilshhelp)
        await asyncio.sleep(30)
        await client.delete_message(utils)

    # COMANDO 3.1
    elif message.content.startswith("s!convite"):
        # await client.delete_message(message)

        temp = await client.send_message(message.author,
                                         "<:sesho:433317803328536576> Convite criado " + message.content[8:] + ".")
        try:
            invite = await client.create_invite(message.channel, max_uses=2, temporary=True, xkcd=True)
            await client.edit_message(temp, "<:sesho:433317803328536576> Convite criado  " + message.content[11:] + str(
                invite))
        except:
            await client.edit_message(temp, ":no_entry: Falha ao criar convite.")

    # COMANDO 3.2
    elif message.content.lower().startswith('s!feedback'):
        await client.delete_message(message)
        await client.send_typing(message.channel)
        fd = message.content[10:]
        channel = client.get_channel("442444721919361024")
        if len(fd) > 1:
            await client.send_message(channel,
                                      "Novo feedback do  " + message.author.name + "#" + message.author.discriminator + " (" + message.author.id + "): ```" + fd + "```")
            await client.send_message(message.channel, "Enviei o feedback para meu Criador.")
        else:
            await  client.send_message(message.channel, "Insira seu feedback.")


    # COMANDO 3.3
    elif message.content.lower().startswith('s!py'):
        usermsgcod = message.content[4:]
        await client.send_message(message.channel,
                                  '<:python:443164241927864359> {} enviou o segunte código:\n```python\n{} \n```'.format(
                                      message.author.mention, usermsgcod))
        await client.delete_message(message)

    # COMANDO 3.4
    elif message.content.lower().startswith('s!js'):

        usermsgcod = message.content[4:]
        await client.send_message(message.channel,
                                  '<:node:443166969605390337> {} enviou o segunte código:\n```javascript\n{} \n```'.format(
                                      message.author.mention, usermsgcod))

        await client.delete_message(message)

    # COMANDO 3.5
    elif message.content.startswith("s!hora"):
        # await client.delete_message(message)
        dt = datetime.datetime.now()
        msg = "`📅 {}/{}/{}` `⏰ {}:{}:{}`".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)
        await client.send_message(message.channel, msg)

    # COMANDO 3.6
    elif message.content.lower().startswith('s!jogo'):

        if message.author.id == '232309115865661440':
            jogo = message.content[6:]
            await client.change_presence(game=discord.Game(name=jogo))
            vag = await client.send_message(message.author, "Você mudou o status do Bot para " + jogo + "!")
            await client.delete_message(vag)
        if not message.author.id == '232309115865661440':
            await client.delete_message(message)
            embed = discord.Embed(
                title='Sem Permissão',
                color=0x83f68a,
            )
            embed.add_field(name='Ha ha', value='‍⚠  So o Vagner pode usar esse comando', inline=False)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.author, embed=embed)


    # COMANDO 3.7
    elif message.content.lower().startswith('s!votar'):
        await client.delete_message(message)
        try:
            msg = message.content[7:]
            embedvote = discord.Embed(
                title="**VOTAÇÃO**"
                , color=0x1CF9FF, description=None
            )
            embedvote.set_thumbnail(url=message.author.avatar_url)
            embedvote.add_field(name='`📝 Votação iniciada por:`', value=message.author.mention, inline=False)
            embedvote.add_field(name='`🖋 Titulo:`', value="{}".format(msg), inline=False)
            await client.send_typing(message.channel)
            gg = await client.send_message(message.channel, embed=embedvote)
            await client.add_reaction(gg, '✔')
            await client.add_reaction(gg, '❌')
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Insira um texto para iniciar a votação")

    # COMANDO 3.8
    elif message.content.lower().startswith('s!membro'):
        await client.delete_message(message)

        try:
            user = message.author
            role = discord.utils.find(lambda r: r.name == "membro", message.server.roles)
            await client.add_roles(user, role)
            mm = await client.send_message(message.channel, 'Cargo adicionado ')
            await asyncio.sleep(20)
            await client.delete_message(mm)
        except Exception:
            await client.send_message(message.channel, "O servidor nao possui o cargo: membro")

    # COMANDO 3.9
    elif message.content.lower().startswith("s!aviso"):
        #  await client.delete_message(message)
        try:
            user = message.author
            msg = message.content[7:]

            embed = discord.Embed(
                title=" :loudspeaker: AVISO :loudspeaker:",
                description="{}".format(msg),
                color=0xe67e22
            )
            embed.set_footer(
                text="Enviado por: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(message.channel, embed=embed)
        finally:
            pass


    # COMANDO 3.10
    elif message.content.lower().startswith("s!tr"):

        await client.send_message(message.channel,
                                  'Selecione uma opçao para traduzir: \n 1: Para o ingles \n 2: Passando linguagem de saida ')
        selection = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)

        translator = Translator()
        msg = 'Ocorreu um error'
        await client.send_message(message.channel, 'insira o texto')
        sentence = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)

        try:
            if (selection.content == '1' or selection.content == '$1'):
                result = translator.translate(sentence.content)
            elif (selection.content == '2' or selection.content == '$2'):
                await client.send_message(message.channel, 'Coloque a linguagem para traduzir')
                destLang = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)
                result = translator.translate(sentence.content, destLang.content)
            else:
                await client.send_message(message.channel, 'Seleção cancelada')
                return
        except:
            await client.send_message(message.channel, 'Erro ao buscar linguagem')
            return
        if (result):
            msg = 'Resultado:  ' + result.text
        await client.send_message(message.channel, msg)
        return

    #  _____   _____   _____   _____   _____   _____   _____   _____   _____
    # |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

    #  _  _             ___            __
    # | || |           |_ _|  _ __    / _|   ___
    # | || |_   _____   | |  | '_ \  | |_   / _ \
    # |__   _| |_____|  | |  | | | | |  _| | (_) |
    #    |_|           |___| |_| |_| |_|    \___/

    # HELP INFO
    elif message.content.lower().startswith("s!infohelp"):
        # await client.delete_message(message)
        infohhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='📖Comandos Info📖')
        infohhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        infohhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        infohhelp.add_field(name='**s!fort**', value='`<usuario texto>Mostra o status do usario no fortnite`',
                            inline=False)
        infohhelp.add_field(name='**s!botinfo**', value='`Mostra informaçoes sobre o bot`', inline=False)
        infohhelp.add_field(name='**s!serverinfo**', value='`mostra informaçoes do servidor`', inline=False)
        infohhelp.add_field(name='**s!userinfo**', value='`[mençao do usuario] Mostra informçoes do uuario`',
                            inline=False)
        infohhelp.add_field(name='**s!emoji**', value='`Exibe os emoji do servidor Info: Menos personalizados`',
                            inline=False)
        infohhelp.add_field(name='**s!noticia**', value='`Exibe um noticia Atual`', inline=False)
        infohhelp.add_field(name='**s!bitcoin**', value='`Exibe o valor atual do bitcoin`', inline=False)
        infohhelp.add_field(name='**s!cargos**', value='`Exibe os cargos do servidor`', inline=False)
        infohhelp.add_field(name='**s!avatar**',
                            value='`[mençao do usuario] Exibe o avatar do usuario mencionado ou o seu`', inline=False)
        infohhelp.add_field(name='**s!uptime**', value='`Exibe a quanto tempo o bot está online`', inline=False)
        infohhelp.add_field(name='**s!user**', value='`<menção do usuario>Exibe informaçoes do usuario mencionado`',
                            inline=False)
        infohhelp.add_field(name='**s!ping**', value='`Exibe o tempo de resposta do bot`', inline=False)
        infohhelp.add_field(name='**s!canal**', value='`Exibe informaçoes do canal atual`', inline=False)
        infohhelp.add_field(name='**s!status**', value='`Exibe Meus status detalhados`', inline=False)
        infohhelp.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                             icon_url=message.author.avatar_url)
        info = await client.send_message(message.author, embed=infohhelp)
        await asyncio.sleep(30)
        await client.delete_message(info)

    # COMANDO 4.1
    elif message.content.lower().startswith('s!fort'):
        #  await client.delete_message(message)
        await client.send_typing(message.channel)
        name = message.content[7:]
        link = "https://fortnitetracker.com/profile/pc/" + name
        url = "https://api.fortnitetracker.com/v1/profile/pc/" + name
        headers = {"TRN-Api-Key": f"{fort_key}"}
        jsonB = requests.get(url, headers=headers)
        json_data = jsonB.json()
        for item in json_data.get("lifeTimeStats"):
            if item['key'] == "Wins":
                wins = item['value']
            if item['key'] == "K/d":
                kd = item['value']
            if item['key'] == "Win%":
                winpercent = item['value']
            if item['key'] == 'Kills':
                kills = item['value']
            if item['key'] == 'Matches Played':
                matches = item['value']
        fort = discord.Embed(title='`FORTNITE STATUS`', description=None, color=0x83f68a)
        fort.set_thumbnail(url='https://i.imgur.com/qef0e2G.png')
        fort.add_field(name='Plataforma ﾠﾠﾠﾠ<:pc:438436463605186562>', value='ﾠ', inline=False)
        fort.add_field(name='👤 | `Nome`', value=name, inline=True)
        fort.add_field(name='🏆 | `Vitorias`', value=wins)
        fort.add_field(name='🛡 | `K/D`', value=kd)
        fort.add_field(name='🔪 | `Kills`', value=kills)
        fort.add_field(name='📊 | `Taxa de vitorias`', value=winpercent)
        fort.add_field(name='🔎 | `Partidas`', value=matches)
        fort.add_field(name='🌐 | `Perfil`', value='[link](' + link + ')\n')
        fort.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                        icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=fort)

    # COMANDO 4.2
    elif message.content.lower().startswith('s!botinfo'):
        #  await client.delete_message(message)

        embedbot = discord.Embed(
            title='**<:230105988211015680:433479568553410561> Info do Bot**',
            color=0x83f68a,
            description='\n'
        )
        embedbot.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
        embedbot.add_field(name='`◼ | Id bot`', value=client.user.id, inline=True)
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name='📛 | Tag', value=client.user)
        embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))
        embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name='‍⚙️ | Programador', value="`Vagner Cavalcante`")
        embedbot.add_field(name='<:python:443164241927864359> | Version', value="`3.6.4`")
        embedbot.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embedbot)

    # COMANDO 4.3
    elif message.content.lower().startswith('s!serverinfo'):
        # await client.delete_message(message)
        try:
            member_list = list(message.server.members)
            status_list = [member.status.value for member in member_list]
            membersinfo = (f"<:313956277808005120:433479572865024020> {status_list.count('online')}"
                           f"<:313956277220802560:433479570642042882> {status_list.count('idle')}"
                           f"<:313956276893646850:433479568628776992> {status_list.count('dnd')}"
                           f"<:313956277237710868:433479571497811988>️{status_list.count('offline')}")
            server = message.server
            text_channels = len([x for x in message.server.channels if x.type == discord.ChannelType.text])
            voice_channels = len([x for x in message.server.channels if x.type == discord.ChannelType.voice])
            passed = (message.timestamp - server.created_at).days
            created_at = ("{}  | Há {} dias!""".format(server.created_at.strftime("%d %b %Y %H:%M"), passed))
            embedbot = discord.Embed(title='`Server Info`', color=0x83f68a, description=None)
            embedbot.set_thumbnail(url=message.server.icon_url)
            embedbot.add_field(name='`☣ | Nome`', value=message.server.name, inline=True)
            embedbot.add_field(name='`👑 | Dono`', value=message.server.owner.mention)
            embedbot.add_field(name='`🕳️ | Id`', value=message.server.id)
            embedbot.add_field(name='`📅 | Criado em`', value=created_at, inline=False)
            embedbot.add_field(name='`👥 | Cargos`', value=len(message.server.roles), inline=True)
            embedbot.add_field(name='`🌐 | Região`', value=message.server.region, inline=True)
            embedbot.add_field(name='`👾 | Canais`', value=(len(list(channel for channel in message.server.channels if
                                                                     channel.type == discord.ChannelType.text or channel.type == discord.ChannelType.voice))),
                               inline=True)
            embedbot.add_field(name='`🧐 | Emojis`', value=(len(message.server.emojis)), inline=True)
            embedbot.add_field(name="`💬 | Canais de Texto`", value=text_channels)
            embedbot.add_field(name="`🗣️ | Canais de Voz`", value=voice_channels)
            embedbot.add_field(name='`🔇 | Canal de afk`', value=message.server.afk_channel, inline=True)
            embedbot.add_field(name='🔐 ﾠ | Segurança', value=message.server.verification_level, inline=True)
            embedbot.add_field(name='`👨‍👦‍👦ﾠ   | Membros`', value=len(message.server.members), inline=True)
            embedbot.add_field(name='`ﾠ👨‍👦‍👦ﾠﾠ  | Membros Status`', value=membersinfo, inline=True)
            embedbot.add_field(name='<:230105988211015680:433479568553410561>   | Bots',
                               value=str(len(list(member for member in message.server.members if member.bot))))
            embedbot.add_field(name='🌀 | Cargo padrão', value=message.server.default_role, inline=True)
            embedbot.add_field(name='📷 | Icon server', value='[Link direto](' + message.server.icon_url + ')\n',
                               inline=True)
            embedbot.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedbot)
        except discord.errors.HTTPException as e:
            await client.send_message(message.channel, "⚠️Erro : {}".format(e))

    # COMANDO 4.4
    elif message.content.lower().startswith('s!userinfo'):
        # await client.delete_message(message)
        try:
            user = message.author
            membro = message.mentions[0]
            embedinfo = discord.Embed(
                title=' informações', color=0x83f68a,
                description='\n ')
            embedinfo.set_thumbnail(url=membro.avatar_url)
            embedinfo.add_field(name='`☣ | Usuário`', value=membro.name)
            embedinfo.add_field(name='`🤬  | Apelido`', value=membro.nick)
            embedinfo.add_field(name='`🕳️ | Id`', value=membro.id)
            embedinfo.add_field(name='`📅 | Desde de`', value=membro.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`🗓️ | Entrou em`', value=membro.joined_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`🎮 | Jogando`', value=membro.game)
            embedinfo.add_field(name='`💎 | Cargos`',
                                value=len(([role.name for role in membro.roles if role.name != "@everyone"])))
            embedinfo.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedinfo)
        except:
            user = message.author
            embedinfo = discord.Embed(
                title=' informações', color=0x83f68a,
                description='\n ')
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='`☣ | Usuário`', value=user.name)
            embedinfo.add_field(name='`🤬  | Apelido`', value=user.nick)
            embedinfo.add_field(name='`🕳️ | Id`', value=user.id)
            embedinfo.add_field(name='`📅 | Desde de`', value=user.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`🗓️ | Entrou em`', value=user.joined_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`🎮 | Jogando`', value=user.game)
            embedinfo.add_field(name='`💎 | Cargos`',
                                value=len(([role.name for role in user.roles if role.name != "@everyone"])))
            embedinfo.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedinfo)

    # COMANDO 4.5
    elif message.content.lower().startswith("s!emoji"):
        # await client.delete_message(message)
        msg = ''
        for emoji in message.server.emojis:
            msg += '<:{0}:{1}> '.format(emoji.name, emoji.id)
        embedmo = discord.Embed(title="Emojis do Servidor  🖥 ️ {} **[{}] Emojis**".format(message.server.name, (
            len(message.server.emojis))), description=msg, color=0x1CF9FF)
        embedmo.set_thumbnail(url=f"{message.server.icon_url}")
        embedmo.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                           icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embedmo)

    # COMANDO 4.6
    elif message.content.lower().startswith('s!noticia'):
        # await client.delete_message(message)
        await client.send_typing(message.channel)
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=globo&apiKey=41e3884b04e24c70a3ae95b99e675a20')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Author:', value="{}".format(authornews))
        embednews.add_field(name='Titulo:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Url da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)

        await client.send_message(message.channel, embed=embednews)

    # COMANDO 4.7

    elif message.content.lower().startswith('s!bitcoin'):
        # await client.delete_message(message)
        await client.send_typing(message.channel)
        imgbtc = ('http://pngimg.com/uploads/bitcoin/bitcoin_PNG47.png')
        try:
            requeget = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=BTC&alt=json')
            btc = json.loads(requeget.text)
            nomebtc = (str(btc['valores']['BTC']['nome']))
            precobtc = (str(btc['valores']['BTC']['valor']))
            fontebtc = (str(btc['valores']['BTC']['fonte']))

            embedbtc = discord.Embed(color=0xffe100, )
            embedbtc.set_author(name='{}'.format(message.author.name),
                                icon_url=message.author.avatar_url)
            embedbtc.add_field(name='Nome:', value="{}".format(nomebtc))
            embedbtc.add_field(name='Valor:', value="{}".format(precobtc))
            embedbtc.add_field(name='fonte:', value="{}".format(fontebtc))
            embedbtc.set_footer(text='Por Vagner')
            embedbtc.set_thumbnail(url=imgbtc)
            await client.send_message(message.channel, embed=embedbtc)
        except:
            await client.send_message(message.channel, 'ERROR!')

    # COMANDO 4.8
    elif message.content.lower().startswith("s!cargos"):
        cargos = [role.name for role in message.server.roles if role.name != "@everyone"]
        role = discord.Embed(title='Cargos do servidor {}'.format(message.server.name),
                             description='Total [{}] Cargos'.format(len(message.server.roles)), color=0x1CF9FF)
        role.set_thumbnail(url=message.server.icon_url)
        role.add_field(name="`Lista`", value='{}'.format(cargos).replace("'", " ").replace("[", " ").replace("]", " "))
        role.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=role)

    # COMANDO 4.9
    elif message.content.lower().startswith('s!avatar'):
        #  await client.delete_message(message)
        try:
            member = message.mentions[0]
            embed = discord.Embed(
                title='📷 Avatar de {}'.format(member.name),
                color=member.color,
                description='[Link direto](' + member.avatar_url + ')\n')

            embed.set_image(url=member.avatar_url)
            embed.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)

        except:
            user = message.author
            embed = discord.Embed(
                title='📷 Seu avatar'.format(user.name),
                color=user.color,
                description='[Link direto](' + user.avatar_url + ')\n')

            embed.set_image(url=user.avatar_url)
            embed.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)

    # COMANDO 4.10
    elif message.content.lower().startswith('s!uptime'):
        #  await client.delete_message(message)
        await client.send_message(message.channel, "`Online a : {0} Horas e {1} Minutos.`".format(hour, minutes))

    # COMANDO 4.11
    elif message.content.lower().startswith('s!user'):
        # await client.delete_message(message)
        try:
            membro = message.mentions[0]
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Nome",
                description=user.name,
                color=0x00000)
            userembed.add_field(name="Informação de usuário ", value='<:423489130899701760:438436463399665664>')
            userembed.set_thumbnail(url=membro.avatar_url)
            userembed.add_field(name="Juntou-se ao servidor em:", value=userjoinedat)
            userembed.add_field(name="Usuário criado em:", value=usercreatedat)
            userembed.add_field(name="TAG:", value=user.discriminator)
            userembed.add_field(name="ID ", value=user.id)
            userembed.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Não consegui encontrar o usuário.")

    # COMANDO 4.12
    elif message.content.lower().startswith('s!ping'):
        # await client.delete_message(message)
        pingtime = time.time()
        e = discord.Embed(title='📡 Esperando resposta do servidor', color=0x1abc9c)
        pingus = await client.send_message(message.channel, embed=e)
        ping = time.time() - pingtime
        ping1 = discord.Embed(title='Pong!', description=':ping_pong: Ping time - `%.01f seconds`' % ping,
                              colour=0x1abc9c)
        ping1.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.edit_message(pingus, embed=ping1)

    # COMANDO 4.13
    elif message.content.lower().startswith('s!canal'):
        # await client.delete_message(message)
        await client.send_typing(message.channel)
        channel = message.channel
        channel = channel or message.channel
        embed = discord.Embed(color=0x83f68a,
                              description=channel.mention)
        embed.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embed.add_field(name="Nome", value=message.channel.name, inline=True)
        embed.add_field(name="Server", value=message.channel.server.name, inline=True)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Posição", value=channel.position + 1)
        embed.add_field(name="Tipo", value=channel.type)
        embed.add_field(name="Criado em", value=message.channel.created_at.strftime("%d %b %Y %H:%M"))
        embed.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)



    # COMANDO 4.14
    elif message.content.startswith('s!status'):
        # await client.delete_message(message)
        link = 'https://discordapp.com/oauth2/authorize?client_id=425670256741187604&permissions=2146958583&scope=bot'
        suport = 'https://discord.gg/brQfChz'
        ram = psutil.virtual_memory().percent
        embed = discord.Embed(title='Sesshomaru Status', color=0x83f68a,
                              description='<:314003252830011395:433479573473067010>`DISCORD STATUS`')
        embed.add_field(name="🌐 Servidores", value="\n```javascript\n{} \n```".format((len(client.servers))))
        embed.add_field(name="👥 Usuarios",
                        value="\n```javascript\n{} \n```".format(len(set(client.get_all_members()))))
        embed.add_field(name="💬 Canais", value="\n```javascript\n{} \n```".format(len(set(client.get_all_channels()))))
        embed.add_field(name='ﾠ', value='<:working:433479573586444290>`CPU STATUS`', inline=False)
        embed.add_field(name="<:memory:443164549151981579> Ram used", value="\n```javascript\n{} mb \n```".format(ram))
        embed.add_field(name="<:cpu:438098135429021696> Cpu used",
                        value="\n```javascript\n{} % \n```".format(str(psutil.cpu_percent(interval=1))))
        embed.add_field(name="⏳ Uptime", value="\n```javascript\n{} hrs {} min \n```".format(hour, minutes))
        embed.add_field(name='ﾠ', value='🔧`DEVELOPER STATUS`', inline=False)
        embed.add_field(name="<:python:443164241927864359>Python Version",
                        value="\n```javascript\n{} \n```".format('3.6.4'))
        embed.add_field(name="📚 Libs", value="\n```javascript\n{} packages \n```".format('14'))
        embed.add_field(name="⚙ Programador", value="\n```javascript\n{} \n```".format('Vagner Cavalcante'))
        embed.add_field(name='ﾠ', value='🔗`OTHERS LINKS`', inline=False)
        embed.add_field(name='<:invite:439158621306093578> | `Invite`', value='[**link**](' + link + ')\n')
        embed.add_field(name='<:gear:439186818433286144> | `Suport Server`', value='[**link**](' + suport + ')\n')
        embed.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                         icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)


    #  _____   _____   _____   _____   _____   _____   _____   _____   _____
    # |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

    #  ____            _____
    # | ___|          |  ___|  _   _   _ __
    # |___ \   _____  | |_    | | | | | '_ \
    #  ___) | |_____| |  _|   | |_| | | | | |
    # |____/          |_|      \__,_| |_| |_|

    # HELP FUN
    elif message.content.lower().startswith("s!funhelp"):
        # await client.delete_message(message)
        funhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='🎉Comandos Fun🎉')
        funhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        funhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        funhelp.add_field(name='**s!loteria**', value='`<numero inteiro>Faz um sorteio de 1 a 100 `', inline=False)
        funhelp.add_field(name='**s!say**', value='`<messagem em texto>Faz o bot enviar sua messagem`', inline=False)
        funhelp.add_field(name='**s!gif**', value='`Envia um gif de bleach`', inline=False)
        funhelp.add_field(name='**s!moeda**', value='`Adcione uma reaction de cara ou coroa`', inline=False)
        funhelp.add_field(name='**s!virus**', value='`<menção usuario>Envia um virus para o usuario mencionado`',
                          inline=False)
        funhelp.add_field(name='**s!loli**', value='`Envia um gif de uma loli`', inline=False)
        funhelp.add_field(name='**s!kagome**', value='`Envia um gif aleatorio da Kagome`', inline=False)
        funhelp.add_field(name='**s!kagome**', value='`Envia um gif aleatorio da Sesshomaru`', inline=False)
        funhelp.add_field(name='**s!abraco**', value='`[menção usuario]Manda um abraço para o usuario mencionado`',
                          inline=False)
        funhelp.add_field(name='**s!dado**', value='`Joga o dado podendo da o resultado de 1 a 6`', inline=False)
        funhelp.add_field(name='**s!neko**', value='`Envia uma neko que pode se alterada reagindo o `', inline=False)
        funhelp.add_field(name='**s!catgif**', value='`Envia um gato em gif`', inline=False)
        funhelp.add_field(name='**s!cat**', value='`Envia a img de um gato`', inline=False)
        funhelp.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                           icon_url=message.author.avatar_url)
        fun = await client.send_message(message.author, embed=funhelp)
        await asyncio.sleep(30)
        await client.delete_message(fun)

    # COMANDO 5.1
    elif message.content.lower().startswith('s!loteria'):
        # await client.delete_message(message)
        try:
            test = int(message.content.strip('s!loteria').strip())
            float(test)
            test += 1
        except ValueError:
            await client.send_message(message.channel, '😝 Escolha um numero e tente a sorte ')
        else:
            number = r.randint(1, 100)
            rol = await client.send_message(message.channel, '🎰 Rodando...')
            s(2)
            if number == int(message.content.strip('s!loteria').strip()):
                await client.edit_message(rol,
                                          '<:bolso3:431265060703174667> | **Ganhou!** o numero foi  ' + str(number))
            else:
                await client.edit_message(rol,
                                          '<:draven:437453920923680768> |️**Perdeu!**. O numero foi ' + str(number))

    # COMANDO 5.2
    elif message.content.lower().startswith('s!say'):
        await client.send_message(message.channel, message.content[5:].replace("@everyone",
                                                                               "Não vou mencionar todo mundo,largue de ser chato"))
        await client.delete_message(message)

    # COMANDO 5.3
    elif message.content.lower().startswith('s!gif'):
        # await client.delete_message(message)
        embgif = discord.Embed(
            title='**BLEACH GIF**',
            color=0x83f68a,
            descriptino=None,
        )
        choice = random.randint(1, 5)
        if choice == 1:
            linkdogif = "https://i.imgur.com/9hA71QO.gif"
        if choice == 2:
            linkdogif = "https://i.imgur.com/mNnptDX.gif"
        if choice == 3:
            linkdogif = "https://i.imgur.com/9PlaFO5.gif"
        if choice == 4:
            linkdogif = "https://media.giphy.com/media/qgj8eOOsNO4qA/giphy.gif"
        if choice == 5:
            linkdogif = "https://i.imgur.com/3RT3PF9.gif"
        embgif.set_image(url=linkdogif)
        embgif.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embgif)

    # COMANDO 5.4
    elif message.content.startswith('s!moeda'):
        # await client.delete_message(message)
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '👑')
        if choice == 2:
            await client.add_reaction(message, '😃')

    # COMANDO 5.5
    elif message.content.lower().startswith('s!virus'):
        # await client.delete_message(message)
        user = message.mentions[0]
        v = await client.send_message(message.channel, "initializing...")
        await asyncio.sleep(3.0)
        await client.edit_message(v, "[▓                         ] / -virus.bat Packing files.")
        await asyncio.sleep(0.5)
        await client.edit_message(v, "[▓▓                    ] - -virus.bat Packing files..")
        await asyncio.sleep(0.7)
        await client.edit_message(v, "[▓▓▓            ] | -virus.bat Packing files..")
        await asyncio.sleep(1.0)
        await client.edit_message(v, "[▓▓▓▓        ] / -virus.bat Packing files..")
        await asyncio.sleep(0.5)
        await client.edit_message(v, "[▓▓▓▓▓    ] - -virus.bat Packing files..")
        await asyncio.sleep(0.8)
        await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
        await asyncio.sleep(4.0)
        await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
        await asyncio.sleep(0.8)
        await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
        await asyncio.sleep(0.5)
        await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
        await asyncio.sleep(1.2)
        await client.edit_message(v, "[▓▓▓▓▓▓] / -virus.bat Packing files..")
        await asyncio.sleep(1.0)
        await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
        await asyncio.sleep(0.8)
        await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
        await asyncio.sleep(0.8)
        await client.edit_message(v, "Successfully downloaded virus...")
        await asyncio.sleep(0.5)
        await client.edit_message(v, "Installing 'Keylogger'...")
        await asyncio.sleep(2.0)
        ss = await client.edit_message(v, "Successfully injected Keylogger into **{}**!".format(user.name))
        await asyncio.sleep(1.0)
        await client.delete_message(ss)

    # COMANDO 5.6
    elif message.content.lower().startswith('s!loli'):
        # await client.delete_message(message)
        embgif = discord.Embed(
            title='Gif....',
            color=0x83f68a,
            descriptino=None,
        )
        imagem = "https://i.imgur.com/SxhMmjb.gif"
        embgif.set_image(url=imagem)
        embgif.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embgif)


    # COMANDO 5.7
    elif message.content.lower().startswith('s!kagome'):
        # await client.delete_message(message)
        gif_tag = "kagome"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    # COMANDO 5.8
    elif message.content.startswith('s!abraco'):
        # await client.delete_message(message)
        arguments = (message.content.split(' ')[1:])
        msg = 'Olá '
        if len(message.mentions) == 1 and len(arguments) == 1:
            bot = discord.utils.get(message.server.members, name='Sesshomaru')
            if message.mentions[0] == message.author:
                msg = "Você é solitario? Entao aqui está um abraço <:sesho:433317803328536576>"
            elif message.mentions[0] == bot:
                msg = "Você me ama <:sesho:433317803328536576>"
            else:
                msg = "{}{}! Você Ganhou um abraço do(a) {} <:sesho:433317803328536576> \n".format(msg,
                                                                                                   message.mentions[
                                                                                                       0].mention,
                                                                                                   message.author.mention)
        elif len(message.mentions) > 1 and len(arguments) == len(message.mentions):
            for member in message.mentions:
                msg = '{}{} '.format(msg, member.mention)
            msg = "{}! Você foi abracado por {} <:sesho:433317803328536576> \n".format(msg, message.author.mention)

        await client.send_message(message.channel, msg)


    # COMANDO 5.9
    elif message.content.startswith("s!dado"):
        # await client.delete_message(message)
        choice = random.randint(1, 6)
        embeddad = discord.Embed(title='🎲 Dado', description=' Joguei o dado, o resultado foi :   {}'.format(choice),
                                 colour=0x1CF9FF)
        await client.send_message(message.channel, embed=embeddad)

    # COMANDO 5.10
    elif message.content.lower().startswith('s!neko'):
        msg1 = await client.send_message(message.channel, a7x())
        op = await client.add_reaction(msg1, "\U000023ed")
    # neko_id = op.id

    # COMANDO 5.11
    elif message.content.lower().startswith('s!catgif'):
        # await client.delete_message(message)
        embgif = discord.Embed(
            title='Gato Gif',
            color=0x83f68a,
            descriptino=None,
        )

        embgif.set_image(url=requests.get('http://thecatapi.com/api/images/get?format=src&type=gif').url)
        embgif.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embgif)

    # COMANDO 5.12
    elif message.content.lower().startswith('s!cat'):
        # await client.delete_message(message)
        embimg = discord.Embed(
            title='Gato',
            color=0x83f68a,
            descriptino=None,
        )
        embimg.set_image(url=requests.get('http://thecatapi.com/api/images/get?format=src&type=jpg').url)
        embimg.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embimg)


    # COMANDO 513
    elif message.content.lower().startswith('s!sesho'):
        #  await client.delete_message(message)
        gif_tag = "sesshomaru"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')


#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|





#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|


#  _____                          _                         _            ____                   _     _
# | ____| __   __   ___   _ __   | |_    ___    ___      __| |   ___    |  _ \    __ _    ___  | |_  (_)   ___    _ __
# |  _|   \ \ / /  / _ \ | '_ \  | __|  / _ \  / __|    / _` |  / _ \   | |_) |  / _` |  / __| | __| | |  / _ \  | '_ \
# | |___   \ V /  |  __/ | | | | | |_  | (_) | \__ \   | (_| | |  __/   |  _ <  | (_| | | (__  | |_  | | | (_) | | | | |
# |_____|   \_/    \___| |_| |_|  \__|  \___/  |___/    \__,_|  \___|   |_| \_\  \__,_|  \___|  \__| |_|  \___/  |_| |_|


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "⏭":
        await client.edit_message(msg, a7x())
    # await client.remove_reaction(msg, "\U000023ed")
    else:
        pass
    if reaction.emoji == "📜" and msg.id == msg_id:
        embtest1 = discord.Embed(
            title=None,
            color=0x1CF9FF,
            descriptino=None, )
        embtest1.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest1.add_field(name='**COMANDOS**', value='📜 Formato on_message', inline=True)
        embtest1.add_field(name='**TOTAL**', value='`47 COMANDOS`', inline=False)
        embtest1.add_field(name='**SOBRE**',
                           value='`Sou apenas um simples bot para discord\nCriado pelo pelo Vagner\nVersão: 2.1`',
                           inline=False)
        # await client.wait_for_reaction('📜', message=msg)
        await client.edit_message(msg, embed=embtest1)

    if reaction.emoji == "🔍" and msg.id == msg_id:
        embtest6 = discord.Embed(
            title='Para mais detalhes `use s!searchhelp`',
            color=0x1CF9FF,
            descriptino=None,
        )
        embtest6.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest6.add_field(name='**🔍 SEARCH**', value='`s!youtube`\n`s!google`', inline=True)
        # await client.wait_for_reaction('🔍', message=msg)
        await client.edit_message(msg, embed=embtest6)

    if reaction.emoji == "⚙" and msg.id == msg_id:
        embtest5 = discord.Embed(
            title='Para mais detalhes `use s!utilshelp`',
            color=0x1CF9FF,
            descriptino=None,
        )
        embtest5.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest5.add_field(name='**⚙️UTILS**',
                           value='`s!sping`\n`s!tr`\n`s!aviso`\n`s!membro`\n`s!feedback`\n`s!convite`\n`s!hora`\n`s!js`\n`s!py`\n`s!jogo`\n`s!votar`',
                           inline=True)

        # await client.wait_for_reaction('⚙', message=msg)
        await client.edit_message(msg, embed=embtest5)

    if reaction.emoji == "📖" and msg.id == msg_id:
        embtest4 = discord.Embed(
            title='Para mais detalhes `use s!infohelp`',
            color=0x1CF9FF,
            descriptino=None,
        )
        embtest4.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest4.add_field(name='**📖 INFO**',
                           value='`s!status`\n`s!mcount`\n`s!canal`\n`s!ping`\n`s!fort`\n`s!bitcoin`\n`s!noticia`\n`s!cargos`\n`s!emoji`\n`s!botinfo`\n`s!serverinfo`\n`s!userinfo`\n`s!avatar`\n`s!uptime`\n`s!user`',
                           inline=True)
        # await client.wait_for_reaction('📖', message=msg)
        await client.edit_message(msg, embed=embtest4)

    if reaction.emoji == "🔐" and msg.id == msg_id:
        embtest3 = discord.Embed(
            title='Para mais detalhes `use s!modhelp`',
            color=0x1CF9FF,
            descriptino=None,
        )
        embtest3.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest3.add_field(name='**🔐 MODERAÇÃO**',
                           value='`s!update`\n`s!getban`\n`s!sban`\n`s!ban2`\n`s!ban`\n`s!apagar`\n`s!mute`\n`s!mutar`\n`s!desmultar`')
        # await client.wait_for_reaction('🔐', message=msg)
        await client.edit_message(msg, embed=embtest3)

    if reaction.emoji == "🎉" and msg.id == msg_id:
        embtest2 = discord.Embed(
            title='Para mais detalhes `use s!funhelp`',
            color=0x1CF9FF,
            descriptino=None,
        )
        embtest2.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        embtest2.add_field(name='**🎉  FUN**',
                           value='`s!sesho`\n`s!cat`\n`s!catgif`\n`s!neko`\n`s!dado`\n`s!abraco`\n`s!kagome`\n`s!loteria`\n`s!say`\n`s!gif`\n`s!moeda`\n`s!virus`\n`s!loli`',
                           inline=True)
        # await client.wait_for_reaction('🎉', message=msg)
        await client.edit_message(msg, embed=embtest2)


#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|


#  _____
# |  ___|  _   _   _ __     ___    ___     ___   ___
# | |_    | | | | | '_ \   / __|  / _ \   / _ \ / __|
# |  _|   | |_| | | | | | | (__  | (_) | |  __/ \__ \
# |_|      \__,_| |_| |_|  \___|  \___/   \___| |___/

def a7x():
    r = requests.get('https://nekos.life/api/neko')
    if r.status_code == 200:
        js = r.json()
        return js['neko']


async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1


client.loop.create_task(uptime())

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|

# sessho token
client.run(token)