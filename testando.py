import time
import discord
from discord.ext.commands import Bot
import asyncio



start_time = time.time()

version = "beta"
#define o prefixo
client = Bot("/")
#para criar teu help personalizado
client.remove_command("help")



@client.event
async def on_ready():
    print("=================================")
    print("Nome: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("On line em : {} Serves".format(str(len(client.servers))))
    print(f"Bot Versão: {version}")
    await client.change_presence(game=discord.Game(name='crescendo', type=0))
    print("=================================")

@client.command(aliases=['p'])
async def ping():
    pingtime = time.time()
    e = discord.Embed(title = 'Ok espere', color = 0x1abc9c)
    pingus = await client.say(embed=e)
    ping = time.time() - pingtime
    ping1 = discord.Embed(title = 'Pong!', description = ':ping_pong: Ping time - `%.01f seconds`' % ping, colour = 0x1abc9c)
    await client.edit_message(pingus, embed=ping1)

@client.command(pass_context=True, aliases=['k'])
async def kick(ctx, *, member: discord.Member = None):
    if not ctx.message.author.bot:
        if not ctx.message.author.server_permissions.administrator:
            return

        if not member:
            return await client.say(ctx.message.author.mention + "marque o membro para expulsar!")
        try:
            await client.kick(member)
        except Exception as e:
            if 'previlegio baixo' in str(e):
                return await client.say(":x: Vc nao tem permissão")

        embed = discord.Embed(description="Expulso!!!" % member.name, color=0x1abc9c)
        return await client.say(embed=embed)


@client.command(pass_context = True)
async def mute(ctx, member : discord.Member, mutetime):
    if not ctx.message.author.server_permissions.administrator:
        return await client.say("Somente adm podem mutar........")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("" + member.mention + " foi mutado por " + mutetime + "!")
    await asyncio.sleep(int(mutetime))
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)


client.run('token aki')