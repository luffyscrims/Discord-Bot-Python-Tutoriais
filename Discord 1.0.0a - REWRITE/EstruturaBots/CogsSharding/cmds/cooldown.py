# -*- coding: utf-8 -*-
"""
Tutorial De coldown para usar no seu bot
~~~~~~~~~~~~~~~~~~~

Exemplo basico de cooldown por comando.

:copyright: (c) 2017 Vagner
:license: MIT .
"""

from discord.ext import commands
import discord

#Basic cooldown usando uma função interna do ext
class cooldown:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #Aqui que acontece a magica
    #vamos aos Parâmetros
    #(quantidade,segundo,por usuario ou guild)
    #O primeiro e a quantidade de usos para disparar o colldown
    #o segundo é quantos segundos o colldown terá
    #o terceiro é para definir o cooldown por usuario ou por guild
    #no exemplo abaixo está : a cada 1 uso do comando o usuario vai ter que esperar 20 segundos para usar o comando novamente
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def cd(self, ctx):
        await ctx.send("testado")

    #aqui vamos definir a messagem de erro por comando
    #você também por definir no evento de error um padrão para todos os comandos
    @cd.error
    async def cd_error(self,ctx,error):
      if isinstance(error, discord.ext.commands.CommandOnCooldown):
        #aqui faremos a conversão do segundos para minutos e horas
        min, sec = divmod(error.retry_after, 60)
        h, min = divmod(min, 60)
        if min == 0.0 and h == 0:
            await ctx.send('**Espere `{0}` segundos . Para usar o comando cd novamente.**'.format(round(sec)))
        else:
            await ctx.send('**Espere `{0}` horas `{1}` minutos  e `{2}` segundos. Para usar o comando cd novamente.**'.format(round(h),round(min),round(sec)))


def setup(bot):
    bot.add_cog(cooldown(bot))
