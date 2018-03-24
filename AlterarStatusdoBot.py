 Types:
 0 = padrao jogando
 1 = transmissão
 2 = ouvindo
 3 = assistindo



exemplo
#colocar no evento async def on_ready():

await client.change_presence(game=discord.Game(name="League of legends", url="https://www.twitch.tv/vagner8k", type=1))
