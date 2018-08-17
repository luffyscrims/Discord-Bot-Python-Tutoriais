from discord.ext import commands
import discord

class info:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def userinfo(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            user = ctx.message.author
        roles = []
        for r in user.roles:
            roles.append(r.name)
            bb = "\n".join(roles)

        embed = discord.Embed(color=user.color, description="Info: {}!".format(user.name))
        embed.title = "{}".format(user)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Nome", value=user.name, inline=True)
        embed.add_field(name="Tag", value=user.discriminator, inline=True)
        embed.add_field(name="ID", value=str(user.id), inline=True)
        embed.add_field(name=f"Cargos [{len(roles)}]", value=bb, inline=True)
        embed.add_field(name="Desde", value=user.created_at.strftime("%d %b %Y %H:%M"), inline=True)
        try:
            embed.add_field(name="Jogando", value=user.game.name, inline=True)
        except:
            pass
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        membros = set(ctx.message.guild.members)
        bots = filter(lambda m: m.bot, membros)
        bots = set(bots)
        em = discord.Embed(title=ctx.message.guild.name, colour=0x2df700)
        em.add_field(name="Dono", value=ctx.message.guild.owner.mention)
        em.add_field(name="ID", value=ctx.message.guild.id, inline=True)
        em.set_thumbnail(url=ctx.message.guild.icon_url)
        em.add_field(name="Cargos", value=len(ctx.message.guild.roles), inline=True)
        em.add_field(name="Mebros", value=len(ctx.message.guild.members), inline=True)
        em.add_field(name="Bots", value=len(bots), inline=True)
        em.add_field(name="Criado em",value=ctx.message.guild.created_at.strftime("%d %b %Y %H:%M"))
        em.add_field(name="Região", value=str(ctx.message.guild.region).title())
        await ctx.send(embed=em)




def setup(bot):
    bot.add_cog(info(bot))